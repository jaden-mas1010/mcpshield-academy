"""Standalone tests for actual student policies and grading (no MCP/LLM needed)."""
import copy
import json
import pytest
from student_lab import LABS, grade, public_lab


def fixed(mission):
    p = copy.deepcopy(LABS[mission]['starter'])
    if mission == 1:
        p['enforce_owner_for_analyst'] = True
    elif mission == 2:
        p['verify_description'] = True
        p['allow_unknown_tools'] = False
    elif mission == 3:
        p['allow_tool_response_commands'] = False
        p['require_human_approval_for'] = ['close_alert']
    elif mission == 4:
        p['agent_tools'] = ['read_alert', 'summarize_alert']
    elif mission == 5:
        p['repeated_denials_threshold'] = 3
        p['flag_tampered'] = True
        p['privileged_tools'] = ['close_alert', 'delete_alert', 'export_database']
    return p


@pytest.mark.parametrize('mission', [1, 2, 3, 4, 5])
def test_insecure_starter_does_not_pass(mission):
    p = LABS[mission]['starter']
    response = grade(mission, json.dumps(p), LABS[mission]['answer'])
    assert response['completed'] is False
    assert response['passed'] < response['total']


@pytest.mark.parametrize('mission', [1, 2, 3, 4, 5])
def test_actual_policy_fix_is_validated(mission):
    p = fixed(mission)
    response = grade(mission, json.dumps(p), LABS[mission]['answer'])
    assert response['completed'] is True, response
    assert response['passed'] == response['total']
    assert response['score'] == 100


def test_only_observing_demo_does_not_grant_completion():
    response = grade(1, json.dumps(fixed(1)), None)
    assert response['score'] == 100
    assert response['completed'] is False


def test_schema_validation_rejects_lie_fields():
    policy = fixed(4)
    policy['completed'] = True
    with pytest.raises(ValueError):
        grade(4, json.dumps(policy), 1)


def test_broken_json_returns_actionable_error():
    with pytest.raises(ValueError, match='Invalid JSON'):
        grade(2, '{oops}', 0)


def test_unknown_mission_is_rejected():
    with pytest.raises(ValueError):
        grade(99, '{}', 0)


def test_question_is_part_of_public_lab():
    assert 'question' in public_lab(3)
    assert 'answer' not in public_lab(3)
