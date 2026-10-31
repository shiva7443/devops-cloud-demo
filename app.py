from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.0.1"


@app.route("/")
def home():
    return f"<h1>DevOps and Cloud Integration Demonstrator</h1><p>Version {VERSION} - deployed automatically via GitHub Actions + Docker.</p>"


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
