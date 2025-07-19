from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeCompleto = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)

    def __init__(self, nomeCompleto, cpf, endereco):
        self.nomeCompleto = nomeCompleto
        self.cpf = cpf
        self.endereco = endereco

    def to_dict(self):
        return {
            'id': self.id,
            'nomeCompleto': self.nomeCompleto,
            'cpf': self.cpf,
            'endereco': self.endereco
        }