# Test plan: Flashcards web app

**System under test:** a small Flask flashcard app (`app/`). Pages: card list with an add form, and a quiz page.
**Goal:** check that a user can add, view, delete and quiz cards, and that bad input is handled safely.
**Approach:** requirement-based cases (`test-cases.md`), automated with Playwright and pytest, plus a short exploratory session whose findings are written up as bug reports (`bug-reports.md`).

## In scope
- Adding cards: valid input, empty, whitespace only, length boundary (200 characters), special characters, Danish characters.
- Deleting cards, including an id that does not exist.
- Quiz page: empty state, answer hidden until requested.
- Output encoding (HTML must be shown as text, never executed).

## Out of scope
Performance, accessibility audit, other browsers than Chromium, persistence (cards live in memory by design).

## Entry and exit
Run `python -m pytest` from the project folder. Exit criteria: all automated cases pass and every open finding is written up with steps to reproduce, expected result, actual result and severity.

## Risks
Boundary values and encoding are where small web forms usually fail, so those cases come first.
