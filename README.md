# Web QA Suite

A small web QA project: a test plan, 12 test cases, automated browser tests and written bug reports for a flashcard
web app. I built the app so there is something real to test, then tested it the way a QA colleague would: from the
requirements, from the boundaries, and by exploring.

## Contents

- `docs/test-plan.md`: scope, approach, risks and exit criteria
- `docs/test-cases.md`: 12 cases with steps and expected results
- `tests/test_flashcards.py`: the cases automated with Playwright and pytest (12 tests, all passing)
- `docs/bug-reports.md`: three findings from exploratory testing, each with steps to reproduce, expected result,
  actual result and severity

## Run it

```
pip install flask pytest playwright
playwright install chromium
python -m pytest
```

## What I learned

- Passing tests prove only what they check. All 12 pass, yet exploring found a quiz that cannot move past the first card.
- Boundary values (200 and 201 characters) and special characters are the cheapest places to find defects.
- A good bug report lets someone else reproduce the problem in under a minute.
