"""MISSION 05 — Security monitoring on synthetic MCP audit events.

Student objective: Flag suspicious privileged calls, modified tool metadata,
and 3+ blocked calls to the SAME tool by the SAME actor.
A real service needs trusted, tamper-resistant event collection, time windows,
redaction and alerts shipped to a central monitoring system.
"""


def detect_attack_types(events: list[dict]) -> set[str]:
    """Return rule names for detected security anomalies."""
    findings: set[str] = set()
    # TODO: Detect all three categories while avoiding false positives:
    # EXCESSIVE_PRIVILEGE, TOOL_TAMPERING, REPEATED_DENIALS.
    # BUG: only one privileged tool is checked.
    for event in events:
        if (event.get("role") in {"analyst", "agent"}
                and event.get("tool") == "delete_alert"
                and event.get("decision") == "ALLOWED"):
            findings.add("EXCESSIVE_PRIVILEGE")
    return findings
