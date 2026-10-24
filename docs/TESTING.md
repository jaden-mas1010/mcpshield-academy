# Validation and Testing

## Primary application test suite

From project root:

```powershell
python -m pytest -v --import-mode=importlib
```

Tests cover the five reference mission functions, browser-grade JSON policy repair, evaluator input validation, simulated MCP tool integration (when MCP SDK is installed), dashboard request handling, grading, and reset. **Record the actual numeric test count from your environment; do not cite illustrative counts as verified.**

## Independent hands-on assessment

The browser policy grader is checked by `tests/test_student_lab.py`, including initial insecure conditions and final repaired conditions. The grading API returns named check results and requires a correct knowledge question in addition to behavioural success.

The **advanced source-code track** deliberately begins vulnerable. Run it separately:

```powershell
python -m pytest code_lab/checks_missions.py -v --import-mode=importlib
```

Initial expectation: 5 passed, 5 failed. Student completion goal: 10 passed after correcting source code. **Do not accidentally treat these intentional failures as production test failures.**

## Manual validation checklist

- [ ] Dashboard loads at http://127.0.0.1:8088.
- [ ] All five mission cards and the Student Workshop appear.
- [ ] Vulnerable/secure comparisons work and display different outcomes where appropriate.
- [ ] Insecure JSON starters fail at least one named check in each mission.
- [ ] Repaired JSON policies pass all checks.
- [ ] Correct knowledge check is required to mark a mission complete.
- [ ] Reset starter returns a policy to the deliberately insecure state.
- [ ] `python grade_mission01.py` returns 100/100 for the secure reference implementation.
- [ ] MCP Inspector can list and run `read_alert` on port 8000.
- [ ] `investigate_security_logs` returns 3 findings from 6 synthetic events.
- [ ] Docker compose startup and shutdown work on the target machine.
- [ ] No password, token or sensitive file is in the repository.

## Evidence to include

Screenshots of mission overview, failed policy checks, successful checks, MCP Inspector tool response and test summary. Optional 2–3 minute video with screen recordings. Screenshots committed under `screenshots/` must not include real credentials or private data.

## Important boundaries

Unit tests validate Python functions, not the full authenticated MCP lifecycle. Docker build/runtime tests must be run on a machine with Docker. Tests are not evidence of a real LLM jailbreak; Mission 03 is intentionally deterministic.


## Five-mission coding track

These tests are **intentionally failing until students fix the Python starter files**. They are not part of the normal reference application pass/fail test suite.

```powershell
python -m code_lab.runner --mission 1
python -m code_lab.runner
```

Expected starter state: 8/23 pass, 15/23 fail. Instructor reference solutions: 23/23 pass (independently checked). Browser grading covers JSON policies only, not Python source. Do not claim these educational functions are production-ready.
