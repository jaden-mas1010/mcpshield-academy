"""MCPShield: locally hosted MCP security training server (synthetic data only).

Never expose deliberately vulnerable modes to public networks. LAB_ROLE/LAB_USER are
server-wide classroom configuration, not authenticated per-user credentials.
"""
import os
from mcp.server import MCPServer
from missions.mission01 import can_read_alert
from missions.mission02 import verify_tool
from missions.mission03 import ATTACK_PAYLOAD, process_tool_response
from missions.mission04 import evaluate_tool_request
from missions.mission05 import AUDIT_EVENTS, detect_threats

mcp = MCPServer('MCPShield Lab')

ALERTS = {
    'ALERT-001': {'username':'student01','source_ip':'192.0.2.10','severity':'HIGH','status':'OPEN','assigned_to':'alice'},
    'ALERT-002': {'username':'admin','source_ip':'198.51.100.25','severity':'CRITICAL','status':'OPEN','assigned_to':'bob'},
}
ROLE_PERMISSIONS = {'analyst': {'read_alert'}, 'supervisor': {'read_alert','close_alert'}}
LAB_ROLE = os.getenv('LAB_ROLE', 'analyst')
LAB_USER = os.getenv('LAB_USER', 'alice')
LAB_MODE = os.getenv('LAB_MODE', 'secure')


def is_allowed(action: str) -> bool:
    return action in ROLE_PERMISSIONS.get(LAB_ROLE, set())


@mcp.tool()
def read_alert(alert_id: str) -> dict:
    """Retrieve one synthetic alert subject to the configured classroom policy."""
    if not is_allowed('read_alert'):
        return {'error': 'Permission denied'}
    alert = ALERTS.get(alert_id)
    if alert is None:
        return {'error': 'Alert not found'}
    if LAB_MODE == 'vulnerable':
        return alert.copy()
    if not can_read_alert(LAB_ROLE, LAB_USER, alert):
        return {'error': 'Permission denied'}
    return alert.copy()


@mcp.tool()
def close_alert(alert_id: str) -> dict:
    """Close synthetic alert (role check before changing the in-memory store)."""
    if not is_allowed('close_alert'):
        return {'error': 'Permission denied'}
    if alert_id not in ALERTS:
        return {'error': 'Alert not found'}
    ALERTS[alert_id]['status'] = 'CLOSED'
    return {'alert_id': alert_id, 'message': 'Alert closed successfully'}


@mcp.tool()
def inspect_tool_metadata(description: str) -> dict:
    """Mission 02: check read_alert description against a trusted local manifest."""
    tool = {'name':'read_alert', 'description':description}
    trusted = verify_tool(tool)
    return {'trusted':trusted, 'tool':'read_alert', 'status':'ACCEPTED' if trusted else 'REJECTED'}


@mcp.tool()
def simulate_indirect_injection(mode: str = 'secure') -> dict:
    """Mission 03: deterministic demonstration; no actual LLM execution."""
    return process_tool_response(ATTACK_PAYLOAD, mode)


@mcp.tool()
def simulate_tool_permissions(tool_name: str, mode: str = 'secure') -> dict:
    """Mission 04: evaluate whether a simulated tool action is permitted."""
    return evaluate_tool_request(tool_name, mode)


@mcp.tool()
def investigate_security_logs() -> dict:
    """Mission 05: detect suspicious patterns in six synthetic audit events."""
    alerts = detect_threats(AUDIT_EVENTS)
    return {'events_analysed':len(AUDIT_EVENTS),'threats_detected':len(alerts),'alerts':alerts}


if __name__ == '__main__':
    print(f'MCPShield role={LAB_ROLE} user={LAB_USER} mode={LAB_MODE}', flush=True)
    mcp.run(transport='streamable-http', host=os.getenv('MCP_HOST','127.0.0.1'), port=8000)
