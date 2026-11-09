"""Automated checks mapped to the cases in docs/test-cases.md (TC ids in the test names)."""
from playwright.sync_api import Page, expect


def add(page: Page, q: str, a: str):
    page.fill("#question", q)
    page.fill("#answer", a)
    page.click("text=Add card")


def test_tc01_add_valid_card(page: Page):
    add(page, "What is DNS?", "Maps names to IP addresses")
    expect(page.locator("#count")).to_have_text("1 card")
    expect(page.locator(".q")).to_have_text("What is DNS?")


def test_tc02_empty_fields_show_error(page: Page):
    add(page, "", "")
    expect(page.locator("#error")).to_have_text("Question and answer are required")
    expect(page.locator("#count")).to_have_text("0 cards")


def test_tc03_whitespace_only_is_rejected(page: Page):
    add(page, "   ", "   ")
    expect(page.locator("#error")).to_be_visible()


def test_tc04_boundary_200_chars_accepted_201_rejected(page: Page):
    add(page, "q" * 200, "a")
    expect(page.locator("#count")).to_have_text("1 card")
    add(page, "q" * 201, "a")
    expect(page.locator("#error")).to_have_text("Maximum 200 characters")
    expect(page.locator("#count")).to_have_text("1 card")


def test_tc05_html_is_escaped_not_executed(page: Page):
    add(page, "<script>window.pwned=1</script>", "<b>bold</b>")
    assert page.evaluate("window.pwned") is None
    expect(page.locator(".q")).to_have_text("<script>window.pwned=1</script>")
    expect(page.locator(".a")).to_have_text("<b>bold</b>")


def test_tc06_unicode_and_danish_characters(page: Page):
    add(page, "Hvad hedder æ, ø og å?", "Danske bogstaver ✓")
    expect(page.locator(".q")).to_have_text("Hvad hedder æ, ø og å?")


def test_tc07_delete_removes_only_that_card(page: Page):
    add(page, "one", "1")
    add(page, "two", "2")
    page.locator("li", has_text="one").get_by_role("button", name="Delete").click()
    expect(page.locator("#count")).to_have_text("1 card")
    expect(page.locator(".q")).to_have_text("two")


def test_tc08_quiz_empty_state(page: Page, base_url):
    page.goto(base_url + "/quiz")
    expect(page.locator("#empty")).to_be_visible()


def test_tc09_quiz_hides_answer_until_requested(page: Page, base_url):
    add(page, "Capital of Denmark?", "Copenhagen")
    page.goto(base_url + "/quiz")
    expect(page.locator("#answer")).to_be_hidden()
    page.click("#show")
    expect(page.locator("#answer")).to_be_visible()


def test_tc10_order_is_preserved(page: Page):
    for i in range(3):
        add(page, f"q{i}", f"a{i}")
    expect(page.locator(".q")).to_have_text(["q0", "q1", "q2"])


def test_tc11_direct_post_with_missing_fields_does_not_crash(page: Page, base_url):
    r = page.request.post(base_url + "/cards", data={}, max_redirects=0)
    assert r.status == 302


def test_tc12_unknown_delete_id_is_harmless(page: Page, base_url):
    add(page, "keep", "me")
    r = page.request.post(base_url + "/cards/999/delete", max_redirects=0)
    assert r.status == 302
    expect(page.locator("#count")).to_have_text("1 card")
