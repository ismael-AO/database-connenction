from flask import Flask, request, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:docker@flask_db:5432/flask_database"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    endereco = db.Column(db.String())

    def __init__(self, name, email, endereco):
        self.name = name
        self.email = email
        self.endereco = endereco


class UserSerializer(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "endereco")


db.create_all()


@app.route("/", methods=["GET"])
def index():

    user = Users.query.all()
    print(user)

    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    data = json.loads(request.data.decode("utf-8"))
    
    try:
        new_user = Users(name=data['name'], email=data['email'], endereco=data['endereco'])
        db.session.add(new_user)
        db.session.commit()

        user_query = Users.query.all()
        user_serializer = UserSerializer(many=True)

        user = user_serializer.dump(user_query)

        print(user)

        return make_response(jsonify({"message":"Usuario cadastrado com sucesso", "users": user}), 200)
    except Exception as ex:
        print(ex)
        return make_response(jsonify({"message": " Erro ao cadastrar usuário"}), 403)


if __name__ == "__main__":
    app.run(host='0.0.0.0',  port=3001, debug=True)
