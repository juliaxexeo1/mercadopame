from flask.wrappers import Request
from app.Cliente.model import Cliente
from flask import request,jsonify
from flask.views import MethodView
from app.extensions import db

class ClienteCreate(MethodView):#'/cliente/create'
    def get(self):
        cliente = Cliente.query.all()
        return jsonify ([cliente.json()for cliente in cliente]),200

    def post(self):

        dados = request.json

        nome = dados.get('nome')
        cpf = dados.get('cpf')
        endereco = dados.get('endereco')
        email = dados.get('email')

        #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'}
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'}
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'}

        elif not isinstance (email,str):
            return{'error':'email invalido'}
        
        cliente = Cliente(nome=nome,cpf=cpf,endereco=endereco,email=email)
        db.session.add(cliente)
        db.session.commit()

        return cliente.json(),200

class ClientesDetails(MethodView):#'/cliente/details/<int:id>'
   
    def get (self,id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json(),200
    
#fazer validação de dados
    def put (self,id):
        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome')
        cpf = dados.get('cpf')
        endereco = dados.get('endereco')
        email = dados.get('email')


         #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'}
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'}
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'}
        elif not isinstance (email,str):
            return{'error':'email invalido'}

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
       

        db.session.commit()

        return cliente.json(),200
    
#fazer validação de dados
    def patch(self,id):
        cliente = Cliente.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome',cliente.nome)
        cpf = dados.get('cpf',cliente.cpf)
        endereco = dados.get('endereco',cliente.endereco)
        email = dados.get('email',cliente.email)

         #validação de dados
        if not isinstance(nome,str): 
            return{'error':'nome invalido'}
        elif not isinstance (cpf,int):
            return{'error':'cpf invalido'}
        elif not isinstance(endereco,str):
            return{'error':'endereco invalido'}
        elif not isinstance (email,str):
            return{'error':'email invalido'}

        cliente.nome = nome
        cliente.cpf = cpf
        cliente.endereco = endereco
        cliente.email = email
       

        db.session.commit()

        return cliente.json(),200

    def delete(self,id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente.json(),200



