from flask import request
from app import app
from models import produtos

"""
POST /produto/save (criar produto)
PUT /produto/{id}/update (atualizar produto)
GET /produto/{id} (busca um produto)
GET /produto/all (busca todos os produto)
DELETE /produto/{id}/delete (deletar produto)
POST /carrinho/addProduto/{id}?quantidade={quantidade} (adicionar produto no carrinho)
DELETE /carrinho/removerProduto/1?quantidade={quantidade} (remover produto do carrinho)
DELETE /carrinho/limpar (remover todos os produtos do carrinho)
GET /carrinho/mostrar (busca o carrinho
"""

#Mensagem de boas vindas na raiz (/)
@app.route("/")
def home():
    return{"messagem": "Bem vindo a api-carrinho"}

#Mostrar lista de produtos
@app.route("/produtos", methods=["GET"])
def get_produtos():
    return {"PRODUTOS": produtos}

@app.route("/produtos", methods=["POST"])
def post_produtos():
    novo_produto = request.json
    produtos.append(novo_produto)
    return novo_produto
