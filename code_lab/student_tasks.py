"""MCPShield code lab — intentionally insecure starter functions.

STUDENT INSTRUCTIONS: Fix these five functions. Do not edit the tests.
All resources and audit events are synthetic; no production tools are used.
"""


def can_read_alert(role: str, user: str, alert: dict) -> bool:
    """Mission 01: Analysts must only read alerts assigned to them."""
    # VULNERABILITY: role alone is not sufficient.
    return role in {"analyst", "supervisor"}


def tool_is_trusted(tool: dict, trusted_descriptions: dict) -> bool:
    """Mission 02: Detect changed tool descriptions and unknown tools."""
    # VULNERABILITY: trusts a tool name without checking its description.
    return tool.get("name") in trusted_descriptions


def agent_action_allowed(source: str, action: str, approved: bool) -> bool:
    """Mission 03: Retrieved content may not authorise privileged tool calls.

    source is 'trusted_request' or 'tool_response'; approval is pre-verified
    upstream for this isolated exercise.
    """
    # VULNERABILITY: untrusted log text can order administrative actions.
    return action in {"summarize_alert", "close_alert"}


def agent_tool_granted(tool: str) -> bool:
    """Mission 04: A summary-only agent should have minimal tool grants."""
    # VULNERABILITY: unnecessary administrative permissions.
    return tool in {"read_alert", "summarize_alert", "close_alert", "delete_alert", "export_database"}


def detect_attack_types(events: list[dict]) -> set[str]:
    """Mission 05: Detect excess privilege, tampering, and denial bursts.

    Trigger on three or more BLOCKED attempts to the SAME tool by the SAME actor.
    Only analysts and agents are restricted for privileged tool use.
    """
    findings = set()
    for event in events:
        # VULNERABILITY: inadequate monitoring ignores two important threats.
        if (event["role"] in {"analyst", "agent"}
                and event["tool"] == "delete_alert"
                and event["decision"] == "ALLOWED"):
            findings.add("EXCESSIVE_PRIVILEGE")
    return findings
