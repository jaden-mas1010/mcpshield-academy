# MCPShield — Five Hands-On Python Security Coding Missions

**You write real Python; the lab grades behavior, not button clicks.** Each mission has its own starter file and automated tests. The tests are intentionally red at first.

## Prerequisites

- Python 3.11+ and pytest installed in `.venv`
- Your own computer or dedicated training container; never run untrusted student submissions in a shared backend
- Run commands from the project root (`REDKROSS PROJECT`)

### Quick start — Windows PowerShell

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m code_lab.runner --mission 1
```

1. Open `code_lab/challenges/mission01.py` in VS Code.
2. Read the `TODO` and identify what security check is missing.
3. Edit **only** the student's challenge file. Keep function name and arguments unchanged.
4. Rerun the command until tests pass; verify allowed AND denied behavior.
5. Repeat for missions 02 to 05, substituting `--mission 2` etc.
6. When you are ready: `python -m code_lab.runner` runs all five coding missions.

You may open `http://127.0.0.1:8088` for the animated dashboard. Under **Python Defence Engineering**, select a mission, edit the scratchpad and download `missionNN.py`. **Save it into `code_lab/challenges/` yourself**. The dashboard DOES NOT execute your Python or automatically save it to your machine.

## Exercises

| Mission | File | Student must implement | Production skill |
|---|---|---|---|
| 01 Object authorisation | `mission01.py` | Check assigned owner + role, deny missing values | Per-request, object-level access checks using verified identity |
| 02 Tool metadata | `mission02.py` | Check complete definition against protected manifest | Tool provenance, schema review and metadata pinning |
| 03 Prompt injection | `mission03.py` | Prevent untrusted data from approving privileged actions | Tool-executor authorisation and out-of-band human consent |
| 04 Least privilege | `mission04.py` | Restrict a SOC summariser to its two safe tools | Scoped grants and per-tool enforcement |
| 05 Audit detection | `mission05.py` | Find 3 threat types without raising false positives | Trusted structured logging, SIEM/alert rules and tuning |

There are **23 checks total**. The vulnerable starter deliberately fails **15** of them; 8 checks pass to confirm legitimate functionality. The instructor reference solutions pass **23/23**.

### Run only one mission

```powershell
python -m code_lab.runner --mission 3
```

Or directly:

```powershell
python -m pytest code_lab/tests/test_mission03.py -v --import-mode=importlib
```

### Reset one mission (creates backup)

```powershell
python -m code_lab.reset --mission 3 --yes
```

The prior code is backed up inside `.lab-backups/coding/` (excluded from Git).

## Learning assessment

To count a mission as complete, students should be able to:

- Explain the violated trust boundary in a sentence.
- Show a failing test on the vulnerable starter.
- Implement a Python fix and obtain all passing tests.
- Explain why both an authorised and an unauthorised example were tested.
- Describe what must change in production (see [Production Bridge](PRODUCTION_BRIDGE.md)).

**Important:** Passing these educational tests does not mean the student's code is production-ready. Real deployment needs full authenticated identities, protected configuration, threat modelling, isolation, external security review, and end-to-end integration tests.
