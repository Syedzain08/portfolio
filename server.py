from flask import Flask, render_template, url_for, Response
from flask_frozen import Freezer


app = Flask(__name__)
freezer = Freezer(app)


# --- Index Route --- #
@app.route("/")
def index():
    return render_template("index.html")


# --- Sitemap Route---- #
@app.route("/sitemap.xml")
def sitemap():
    urls = [
        {"loc": url_for("index", _external=True), "priority": "1.0"},
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{url['loc']}</loc>")
        xml.append(f"    <priority>{url['priority']}</priority>")
        xml.append("  </url>")
    xml.append("</urlset>")

    return Response("\n".join(xml), mimetype="text/xml")


if __name__ == "__main__":
    app.config["FREEZER_BASE_URL"] = "https://szain.co"
    freezer.init_app(app)
    freezer.freeze()
