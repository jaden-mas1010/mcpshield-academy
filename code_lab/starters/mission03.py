"""MISSION 03 — Indirect prompt injection vs trusted approval.

Student objective: Never let an MCP tool response grant administrative rights.
This is a deterministic simulation; no LLM is required.
The approved boolean here is a VERIFIED human approval provided by a trusted
workflow. Never take approval or source from the untrusted tool response.
"""


def authorize_agent_action(source: str, action: str, approved: bool) -> bool:
    """Decide whether the tool executor should permit an action."""
    # TODO: Only summarisation is allowed from untrusted tool responses.
    # Closing requires a trusted request AND independent approval.
    # BUG: malicious log text can command the close_alert tool.
    return action in {"summarize_alert", "close_alert"}
