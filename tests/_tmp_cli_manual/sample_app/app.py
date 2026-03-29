"""
sample_app — BrickflowUI Databricks App

Run locally:  brickflowui dev
Deploy:       Zip this folder and upload to Databricks Apps
"""

import brickflowui as db

app = db.App(title="sample_app")


@app.page("/", title="Home", icon="Home")
def home():
    count, set_count = db.use_state(0)

    def increment():
        set_count(count + 1)

    def decrement():
        set_count(count - 1)

    return db.Column([
        db.Text("sample_app", variant="h1"),
        db.Divider(),
        db.Card(
            title="Interactive Counter",
            children=[
                db.Text(f"Current count: {count}", variant="h3"),
                db.Spacer(2),
                db.Row([
                    db.Button("− Decrement", on_click=decrement, variant="secondary"),
                    db.Button("+ Increment", on_click=increment),
                    db.Button("Reset", on_click=lambda: set_count(0), variant="ghost"),
                ]),
            ],
        ),
        db.Spacer(4),
        db.Alert("Edit app.py to start building your Databricks App!", type="info"),
    ], padding=6)


if __name__ == "__main__":
    app.run()
