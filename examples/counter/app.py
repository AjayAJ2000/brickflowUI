"""
Counter example — the simplest possible BrickflowUI app.

Run: python app.py
Open: http://localhost:8050
"""

import brickflowui as db

app = db.App(title="Counter")


@app.page("/", title="Counter", icon="Hash")
def counter_page():
    count, set_count = db.use_state(0)

    def increment():
        set_count(count + 1)

    def decrement():
        set_count(count - 1)

    return db.Column([
        db.Text("Counter", variant="h1"),
        db.Text("A minimal BrickflowUI demo", variant="body", muted=True),
        db.Divider(),
        db.Card(
            children=[
                db.Text(f"{count}", variant="h1"),
                db.Spacer(2),
                db.Row([
                    db.Button("−", on_click=decrement, variant="secondary"),
                    db.Button("+", on_click=increment),
                    db.Button("Reset", on_click=lambda: set_count(0), variant="ghost"),
                ]),
            ],
            title="Current Count",
        ),
        db.Spacer(4),
        db.Row([
            db.Badge(f"Count: {count}", color="blue" if count >= 0 else "red"),
            db.Badge("Running locally", color="green"),
        ]),
    ], padding=6)


if __name__ == "__main__":
    app.run()
