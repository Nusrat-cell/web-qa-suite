# Bug reports from exploratory testing

Each report: title, severity, steps to reproduce, expected, actual, notes.

## BUG-001: Quiz only ever shows the first card
**Severity:** High (the quiz feature cannot be used with more than one card)
**Steps:** 1. Add three cards. 2. Open "Start quiz". 3. Look for a way to see the second card.
**Expected:** A "Next" control moves through all cards.
**Actual:** Only the first card is shown. There is no next control and a reload shows the same card.
**Notes:** Found by reading the quiz page behaviour against the purpose of a quiz. The template renders `cards[0]` only.

## BUG-002: Typed text is lost after a validation error
**Severity:** Medium
**Steps:** 1. Type a long question. 2. Leave the answer empty. 3. Click Add card.
**Expected:** The error appears and the question stays in the field.
**Actual:** The page reloads with the error and both fields are empty, so the user has to type the question again.
**Notes:** The validation error is sent through a redirect, which drops the form values.

## BUG-003: Error message returns when the page is reloaded or bookmarked
**Severity:** Low
**Steps:** 1. Submit an empty form so the error appears. 2. Reload the page.
**Expected:** The error disappears after the next load.
**Actual:** The error stays, because the message is carried in the address (`/?error=...`). Anyone who edits the address can also show any text in the error area, so the message should be chosen from a fixed list instead of taken from the URL.
**Notes:** Output is escaped (TC05 passes), so this is not script injection, but it is a content spoofing risk.
