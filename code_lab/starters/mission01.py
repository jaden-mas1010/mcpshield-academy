"""MISSION 01 — Object-level authorization (BOLA / IDOR).

Student objective: Analysts may read only their assigned alerts. A supervisor
may read any alert. Unknown roles and missing owners must be denied.
The user/role and alert values passed here are TRUSTED server-side fixtures.
"""


def can_read_alert(role: str, user_id: str, alert: dict) -> bool:
    """Return True only if this authenticated actor may read this alert."""
    # TODO: Check the role AND the alert's assigned_to field.
    # BUG: An analyst currently sees every alert, including Bob's.
    return role in {"analyst", "supervisor"}
