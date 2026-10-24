"""Read-only coding catalog: no web endpoint runs student Python."""
from pathlib import Path
import pytest
from code_lab.catalog import MISSIONS, public_code_mission


def test_five_local_python_exercises_exist():
    assert set(MISSIONS) == {1, 2, 3, 4, 5}
    for i in MISSIONS:
        item = public_code_mission(i)
        assert "def " in item["code"]
        assert item["path"].endswith(f"mission{i:02}.py")
        assert item["command"].endswith("--import-mode=importlib")


def test_unknown_mission_rejected():
    with pytest.raises(ValueError):
        public_code_mission(99)


def test_browser_code_api_is_read_only():
    from dashboard import Handler
    assert not any(name in Handler.do_POST.__code__.co_consts for name in ("/api/execute", "/api/run-python"))
