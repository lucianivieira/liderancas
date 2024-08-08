from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost/dbname"
db = SQLAlchemy(app)

class Associado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    secao = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(100), nullable=False)
    lider = db.Column(db.Integer, db.ForeignKey("lider.id"))
    coordenador = db.Column(db.Integer, db.ForeignKey("coordenador.id"))

class Lider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    secao = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(100), nullable=False)

class Coordenador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    secao = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(100), nullable=False)

@app.route("/associados", methods=["GET"])
def get_associados():
    associados = Associado.query.all()
    return jsonify([associado.to_dict() for associado in associados])

if __name__ == "__main__":
    app.run()
