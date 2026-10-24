"""Mission 02: verify tool metadata against a trusted local manifest."""
TRUSTED_TOOLS = {
    'read_alert': 'Read a security alert by ID.',
    'close_alert': 'Close an authorised security alert.',
}


def verify_tool(tool: dict) -> bool:
    name = tool.get('name')
    description = tool.get('description')
    return name in TRUSTED_TOOLS and description == TRUSTED_TOOLS[name]
