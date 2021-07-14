from app.extensions import db

class Cliente(db.Model):
    __tablename__='cliente'
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(100),nullable=False)
    cpf=db.Column(db.Integer,nullable=False, unique=True)
    endereco=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False, unique=True)

    produto=db.relationship('Produto',backref='cliente')

    
    def json(self):
        return{
        'nome':self.nome,
        'cpf':self.cpf,
        'endereco':self.endereco,
        'email':self.email}


