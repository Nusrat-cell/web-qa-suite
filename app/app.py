"""A small flashcard web app used as the system under test."""
from flask import Flask, redirect, render_template, request, url_for

MAX_LEN = 200


def create_app() -> Flask:
    app = Flask(__name__)
    cards: list[dict] = []
    next_id = {"n": 1}

    @app.get("/")
    def index():
        return render_template("index.html", cards=cards, error=request.args.get("error"))

    @app.post("/cards")
    def add_card():
        q = request.form.get("question", "").strip()
        a = request.form.get("answer", "").strip()
        if not q or not a:
            return redirect(url_for("index", error="Question and answer are required"))
        if len(q) > MAX_LEN or len(a) > MAX_LEN:
            return redirect(url_for("index", error=f"Maximum {MAX_LEN} characters"))
        cards.append({"id": next_id["n"], "question": q, "answer": a})
        next_id["n"] += 1
        return redirect(url_for("index"))

    @app.post("/cards/<int:card_id>/delete")
    def delete_card(card_id: int):
        cards[:] = [c for c in cards if c["id"] != card_id]
        return redirect(url_for("index"))

    @app.get("/quiz")
    def quiz():
        return render_template("quiz.html", cards=cards)

    return app
