"""Locally approved complete MCP tool definitions for the teaching exercise."""

READ = {
    "name": "read_alert",
    "description": "Read a security alert by ID.",
    "inputSchema": {"type": "object", "properties": {"alert_id": {"type": "string"}}, "required": ["alert_id"], "additionalProperties": False},
    "annotations": {"readOnlyHint": True},
}
CLOSE = {
    "name": "close_alert",
    "description": "Close an authorised security alert.",
    "inputSchema": {"type": "object", "properties": {"alert_id": {"type": "string"}}, "required": ["alert_id"], "additionalProperties": False},
    "annotations": {"readOnlyHint": False, "destructiveHint": True},
}
APPROVED = {"read_alert": READ, "close_alert": CLOSE}
