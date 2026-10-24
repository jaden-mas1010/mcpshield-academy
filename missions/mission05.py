"""Mission 05: simple deterministic detection of synthetic MCP audit events."""
from collections import Counter

AUDIT_EVENTS = [
    {'id':'E001', 'actor':'alice', 'role':'analyst', 'tool':'read_alert', 'decision':'ALLOWED', 'integrity':'trusted'},
    {'id':'E002', 'actor':'alice', 'role':'analyst', 'tool':'close_alert', 'decision':'BLOCKED', 'integrity':'trusted'},
    {'id':'E003', 'actor':'alice', 'role':'analyst', 'tool':'close_alert', 'decision':'BLOCKED', 'integrity':'trusted'},
    {'id':'E004', 'actor':'alice', 'role':'analyst', 'tool':'close_alert', 'decision':'BLOCKED', 'integrity':'trusted'},
    {'id':'E005', 'actor':'soc-agent', 'role':'agent', 'tool':'export_database', 'decision':'ALLOWED', 'integrity':'trusted'},
    {'id':'E006', 'actor':'soc-agent', 'role':'agent', 'tool':'read_alert', 'decision':'BLOCKED', 'integrity':'tampered'},
]
PRIVILEGED_TOOLS = {'close_alert', 'delete_alert', 'export_database'}


def detect_threats(events: list[dict]) -> list[dict]:
    alerts = []
    blocked_counts = Counter()
    for event in events:
        actor, tool, decision, role = (event[k] for k in ('actor', 'tool', 'decision', 'role'))
        if role in {'analyst','agent'} and tool in PRIVILEGED_TOOLS and decision == 'ALLOWED':
            alerts.append({'type':'EXCESSIVE_PRIVILEGE', 'severity':'HIGH', 'actor':actor, 'evidence':event['id']})
        if decision == 'BLOCKED':
            blocked_counts[(actor,tool)] += 1
        if event.get('integrity') == 'tampered':
            alerts.append({'type':'TOOL_TAMPERING','severity':'HIGH','actor':actor,'evidence':event['id']})
    for (actor,tool), count in blocked_counts.items():
        if count >= 3:
            alerts.append({'type':'REPEATED_DENIALS','severity':'MEDIUM','actor':actor,'evidence':f'{count} blocked calls to {tool}'})
    return alerts

if __name__ == '__main__':
    for alert in detect_threats(AUDIT_EVENTS):
        print(alert)
