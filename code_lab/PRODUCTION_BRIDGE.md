# Bridge from MCPShield Coding Missions to Production Engineering

This is teaching material, not a deployment guide or a security certification. The lab intentionally uses synthetic alerts, fake role strings, fixed policies and simplified log records. Never deploy its intentionally vulnerable code or its server-wide `LAB_ROLE` / `LAB_USER` environment switches as production authentication.

## Mission 01 — BOLA/IDOR → verified principal + trusted ownership

**Lab:** `can_read_alert(role, user_id, alert)` compares the role and `assigned_to`.

**In a real service:** The user ID and role come from a correctly validated identity provider token/session. The alert must be retrieved from the authorised tenant's database or filtered by a database query. Never accept the role/owner from user-supplied JSON.

```python
# Illustrative internal service-layer code. `principal` is produced by trusted
# authentication middleware; `alert` is fetched from a protected database.
def authorize_read(principal, alert):
    if not principal.is_authenticated or principal.tenant_id != alert.tenant_id:
        return False
    if "security_supervisor" in principal.roles:
        return True
    return ("security_analyst" in principal.roles
            and alert.assigned_to == principal.user_id)

# In the HTTP/MCP request handler:
# principal = require_verified_principal(request)  # validated issuer/audience/expiry
# alert = db.load_in_tenant(alert_id, principal.tenant_id)
# if not alert or not authorize_read(principal, alert): deny()
```

Add negative tests for changed tenant, revoked account, missing owner, missing identity, horizontal and vertical privilege escalation.

## Mission 02 — MCP tool poisoning → approve the *whole definition*

**Lab:** check name, description, input schema, annotations and unexpected fields against a trusted manifest.

**In production:** A manifest is reviewed and protected from the MCP server being vetted. Pin the canonical full tool definition (or signed digest). Re-validate when definitions change; treat annotations as hints, not access controls. Also validate the tool server/package provenance and runtime behavior.

```python
import hashlib, json, hmac

def definition_digest(definition: dict) -> str:
    canonical = json.dumps(definition, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

def definition_is_pinned(definition: dict, approved_hashes: dict) -> bool:
    name = definition.get("name")
    expected = approved_hashes.get(name)
    return isinstance(expected, str) and hmac.compare_digest(definition_digest(definition), expected)
```

`approved_hashes` must be obtained from a protected, independently reviewed source; otherwise the attacker can change both the tool and its expected hash.

## Mission 03 — Prompt injection → enforce approval outside the model

**Lab:** `tool_response` cannot approve `close_alert`, even if the text claims it is authorised.

**In production:** Tool responses are untrusted data. A tool executor independently checks the verified principal, authorised purpose/scope, target resource, and a short-lived approval record issued by a trusted workflow. Do not allow prompts or retrieved data to set `approved=True`.

```python
# Illustrative decision logic at tool execution time.
def can_execute_close(principal, alert, approval_store, action="close_alert"):
    return (principal.is_authenticated
            and "close_alert" in principal.scopes
            and alert.tenant_id == principal.tenant_id
            and approval_store.has_valid_approval(
                principal.user_id, action, alert.id
            ))
```

Tool invocation must enforce the decision before changing state, and log approved/denied outcomes without storing secrets.

## Mission 04 — Excessive agency → scoped grants

**Lab:** A SOC summariser receives `read_alert` and `summarize_alert`, nothing more.

**In production:** Bind each tool call to a verified principal and agent/service identity. Use scoped credentials and a separate execution-policy layer. Never interpret model choice of tool as permission to call it.

```python
TOOL_GRANTS = {"soc_summarizer": {"read_alert", "summarize_alert"}}

def authorize_tool(principal, agent_id, tool):
    return (principal.is_authenticated
            and agent_id in principal.permitted_agents
            and tool in TOOL_GRANTS.get(agent_id, set())
            and tool in principal.scopes)
```

Consider step-up authorisation or human confirmation for destructive calls, and use separate credentials for separate MCP servers.

## Mission 05 — Audit detection → structured telemetry with time windows

**Lab:** Detect tool metadata tampering, privilege abuse and three denied requests from the same actor to the same tool.

**In production:** Record a signed/trusted event stream with timestamp, pseudonymous actor, tool ID, decision, correlation ID, policy version and source. Redact secrets and sensitive payloads. Compute denial counts in bounded time windows rather than over all history. Tune for noisy actors, benign retries, and false positives. Send alerts to a SIEM/monitoring pipeline and retain logs under company policy.

**Example event schema (synthetic):**

```json
{"time":"2026-10-24T12:00:00Z","actor_id":"training-user-1","tool":"close_alert","decision":"DENY","reason":"NOT_OWNER","request_id":"training-001","policy_version":"v1"}
```

## Before calling any system production-ready

- Real identity provider / OIDC/OAuth validation (issuer, audience, expiry, scopes)
- Tenant and object-level authorisation, per call, including MCP tools
- Trusted manifests, dependency pinning, change review and supply-chain checks
- Data minimisation, robust input schemas, audit redaction
- Isolation of untrusted MCP processes and any student-supplied code
- Secrets in a secret manager, never checked into Git
- Timeouts, rate limits, process/network permissions and approval workflows
- Integration, abuse-case, end-to-end and regression tests in CI
- Operational alerting, incident response, ownership and code review

Further reading:
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
- [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
