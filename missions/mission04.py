"""Mission 04: tool-grant policy demonstration, no actual destructive actions."""
AVAILABLE_TOOLS = {'read_alert', 'summarize_alert', 'close_alert', 'delete_alert', 'export_database'}
AGENT_ALLOWED_TOOLS = {'read_alert', 'summarize_alert'}


def evaluate_tool_request(tool_name: str, mode: str = 'secure') -> dict:
    if mode not in ('secure', 'vulnerable'):
        raise ValueError('Invalid lab mode')
    if tool_name not in AVAILABLE_TOOLS:
        return {'tool': tool_name, 'status': 'BLOCKED', 'executed': False, 'reason': 'Unknown tool'}
    allowed = mode == 'vulnerable' or tool_name in AGENT_ALLOWED_TOOLS
    return {
        'tool': tool_name,
        'status': 'ALLOWED' if allowed else 'BLOCKED',
        'executed': allowed,
        'reason': 'Tool permitted by policy' if allowed else 'Exceeds agent permissions',
    }
