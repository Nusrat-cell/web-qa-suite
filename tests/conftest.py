import sys
import threading
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from app import create_app  # noqa: E402


@pytest.fixture()
def base_url():
    server = make_server("127.0.0.1", 0, create_app())
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch()
        yield b
        b.close()


@pytest.fixture()
def page(browser, base_url):
    ctx = browser.new_context()
    pg = ctx.new_page()
    pg.goto(base_url)
    yield pg
    ctx.close()
