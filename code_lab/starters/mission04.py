"""MISSION 04 — Least-privilege permissions for agents.

Student objective: The SOC summary agent must only read and summarise alerts.
Unknown agent roles get NO tools. Never trust the model to select its grants.
"""


def agent_tool_allowed(agent_role: str, tool_name: str) -> bool:
    """Return True if this trusted agent role is granted the requested tool."""
    # TODO: Use a small allowlist for the soc_summarizer role and deny others.
    # BUG: the summariser has unnecessary admin capabilities.
    return tool_name in {
        "read_alert", "summarize_alert", "close_alert", "delete_alert", "export_database"
    }
