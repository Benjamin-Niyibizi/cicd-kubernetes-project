"""Inventory application for the CI/CD project."""

from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

VERSION_FILE = Path(__file__).resolve().parent.parent / "VERSION"
APP_VERSION = VERSION_FILE.read_text(encoding="utf-8").strip()

ITEMS = [
    {"id": 1, "name": "Router", "stock": 10},
    {"id": 2, "name": "Switch", "stock": 4},
    {"id": 3, "name": "Network cable", "stock": 25},
]


@app.get("/items")
def get_items():
    """Return all inventory items."""
    return jsonify(ITEMS)


@app.get("/items/<int:item_id>")
def get_item(item_id):
    """Return one item or a 404 response."""
    item = next((item for item in ITEMS if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item)


@app.get("/inventory/summary")
def get_summary():
    """Return the number of items and total stock."""
    return jsonify(
        {
            "item_count": len(ITEMS),
            "total_stock": sum(item["stock"] for item in ITEMS),
        }
    )


@app.get("/health")
def health():
    """Report application health."""
    return jsonify({"status": "ok"})


@app.get("/version")
def version():
    """Report the application version."""
    return jsonify({"version": APP_VERSION})