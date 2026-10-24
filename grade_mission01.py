"""Grade the Python Mission 01 security policy."""
from missions.mission01 import can_read_alert

CASES = [
    ('Analyst own alert', 'analyst', 'alice', {'assigned_to':'alice'}, True),
    ('Analyst cannot read Bob', 'analyst', 'alice', {'assigned_to':'bob'}, False),
    ('Supervisor can read Bob', 'supervisor', 'alice', {'assigned_to':'bob'}, True),
    ('Unknown role denied', 'attacker', 'alice', {'assigned_to':'alice'}, False),
    ('Missing owner denied', 'analyst', 'alice', {}, False),
]


def grade_mission() -> int:
    score = 0
    for name, role, user, alert, expected in CASES:
        try:
            actual = can_read_alert(role, user, alert.copy())
            passed = type(actual) is bool and actual == expected
        except Exception:
            passed = False
        score += 20 if passed else 0
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    print(f'Final Score: {score}/100')
    return score

if __name__ == '__main__':
    raise SystemExit(0 if grade_mission() == 100 else 1)
