import grade_mission01 as grader

def test_secure_policy_scores_100():
    assert grader.grade_mission()==100

def test_insecure_policy_loses_points(monkeypatch):
    monkeypatch.setattr(grader,'can_read_alert',lambda role,user,alert: True)
    assert grader.grade_mission()==40
