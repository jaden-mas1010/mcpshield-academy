from reset_mission01 import reset_mission
import pytest


def test_reset_backups(tmp_path):
    starter=tmp_path/'starter.txt'
    target=tmp_path/'mission.py'
    backups=tmp_path/'backups'
    starter.write_text('vulnerable')
    target.write_text('secure')
    saved=reset_mission(starter,target,backups)
    assert saved.read_text()=='secure'
    assert target.read_text()=='vulnerable'


def test_reset_missing_starter(tmp_path):
    with pytest.raises(FileNotFoundError):
        reset_mission(tmp_path/'missing',tmp_path/'target',tmp_path/'backups')
