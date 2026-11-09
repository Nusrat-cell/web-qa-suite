# Test cases

| ID | Area | Steps | Expected result |
|----|------|-------|-----------------|
| TC01 | Add | Enter a valid question and answer, click Add card | Card appears, counter shows "1 card" |
| TC02 | Add | Submit with both fields empty | Error "Question and answer are required", no card added |
| TC03 | Add | Submit with spaces only | Same error, no card added |
| TC04 | Boundary | Add a 200 character question, then a 201 character question | 200 accepted, 201 rejected with "Maximum 200 characters" |
| TC05 | Security | Add `<script>` and `<b>` as text | Shown literally, script does not run |
| TC06 | Characters | Add text with æ, ø, å and a check mark | Shown unchanged |
| TC07 | Delete | Add two cards, delete the first | Only the second remains |
| TC08 | Quiz | Open the quiz with no cards | Empty message is shown |
| TC09 | Quiz | Open the quiz with one card | Answer hidden until "Show answer" is clicked |
| TC10 | Order | Add three cards | Listed in the order added |
| TC11 | Robustness | POST to /cards without form data | Redirect, no server error |
| TC12 | Robustness | POST delete for an id that does not exist | Redirect, existing cards unchanged |
