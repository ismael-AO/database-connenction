from flask import Flask, request, render_template, make_response, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def calculate():
    data = request.form

    return make_response(jsonify())


if __name__ == "__main__":
    app.run(debug=True)
