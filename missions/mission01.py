"""Mission 01 reference solution. Students repair the separate code_lab tasks."""

def can_read_alert(role: str, user: str, alert: dict) -> bool:
    if role == 'supervisor':
        return True
    if role == 'analyst':
        return bool(user) and alert.get('assigned_to') == user
    return False
