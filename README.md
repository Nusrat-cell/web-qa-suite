# Web QA Suite

A small QA project on a flashcard web app: a test plan, 12 test cases, automated browser tests and three written bug reports.
I built the app first so there was something real to test, then tested it the way a QA colleague would, from the requirements,
from the boundaries (200 and 201 characters, special characters, Danish letters) and by just using it.

- `docs/test-plan.md`: scope, approach, risks, exit criteria
- `docs/test-cases.md`: the 12 cases with steps and expected results
- `tests/test_flashcards.py`: those cases automated with Playwright and pytest
- `docs/bug-reports.md`: three findings, each with steps, expected result, actual result and severity

```
pip install flask pytest playwright
playwright install chromium
python -m pytest
```

## What worked

The boundary cases. Cards of 200 and 201 characters, text with quotes and HTML in it, and Danish letters are quick to write
and are where the app was weakest. The HTML case is the one I would never skip: the app shows `<script>` as text, so
that test passes, and it is why BUG-003 is written up as a spoofing risk and not as script injection.

Writing each bug so someone else can reproduce it in under a minute. The report says what to click, what should have happened
and what did, and BUG-003 says why it matters (the error text is taken from the address bar).

## What did not work

**All 12 automated tests pass and the quiz is still broken.** BUG-001 is a quiz that only ever shows the first card. My quiz
tests cover an empty quiz and a single card, so nothing in the suite ever tried to get to a second one. I found it by using
the app, not by running the tests. That was a hole in my test design, not in the tool, and a test that adds three cards and
steps through them is the one I should have written first. I wrote the bug up instead of closing the gap in the suite, so that
test does not exist yet.

**The bugs are still in the app.** I left them in so the reports can be reproduced. A real project would fix them and keep
each report as a regression test.

**It is slow for what it checks.** The 12 tests take about 10 seconds because each one drives a real browser. That is fine for
12, and it would not stay fine at 200, where most of these should move to checks against the page's HTML and keep only a few
in the browser.

**Only Chromium, and only a desktop window.** The plan lists other browsers, accessibility and performance as out of scope.
Those are the first things a real user would hit that this suite cannot see.
