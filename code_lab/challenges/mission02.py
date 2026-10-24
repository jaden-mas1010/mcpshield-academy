"""MISSION 02 — Detect changes in MCP tool definitions.

Student objective: Allow only approved, UNMODIFIED tool definitions.
In the exercise, approved_manifest is a locally controlled, trusted dict.
Real products require protected manifests, full schema integrity and provenance.
"""


def tool_is_trusted(tool: dict, approved_manifest: dict) -> bool:
    """Decide whether the ENTIRE tool definition matches the approved copy."""
    name = tool.get("name")
    # TODO: Compare all registered metadata, not just the name.
    # BUG: A poisoned description, schema or annotation slips through.
    return name in approved_manifest
