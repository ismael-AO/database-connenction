from flask import Flask, request, render_template, make_response, jsonify
import json
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users(name, password)")
        con.commit()

    return render_template("index.html")


@app.route("/save", methods=["POST"])
def calculate():
    data = json.loads(request.data.decode("utf-8"))
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (name,password) VALUES(?, ?)", (data['value1'], data["value2"]))
            con.commit()

        return make_response(jsonify({"message": "Usuario cadastrado com sucesso"}))
    except Exception as ex:
        return make_response(jsonify({"message": " Erro ao cadastrar usuário"}))


if __name__ == "__main__":
    app.run(debug=True)
