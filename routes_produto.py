from flask import request
from app import app
from models import produtos
from utils import procurar_por_id

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


#Boas Vindas
@app.route("/")
def home():
    return {"mensagem": "Bem Vindo a api-carrinho"}


#Listar todos os produtos
@app.route("/produto/all", methods=["GET"])
def get_produtos():
    return {"PRODUTOS": produtos}


@app.route("/produto/save", methods=["POST"])
def post_produto():
    #dados do json
    dados_json = request.json

    #variável com os dados obrigatórios
    obrigatorio = ["nome", "marca", "preco", "descricao"]
    
    #Verificar se os dados do json vieram com todos os campos obrigatórios.
    #Apenas um produto por vez.
    for dado_obrigatorio in obrigatorio:
        if dado_obrigatorio not in dados_json:
            return {"erro": f"Dado faltando: {dado_obrigatorio}"}, 400 #Error
    
    #Implementação de um id automático
    produto_para_adicionar = {
        "id": len(produtos) + 1,
        "nome": dados_json["nome"],
        "marca": dados_json["marca"],
        "preco": dados_json["preco"],
        "descricao": dados_json["descricao"]
    }
    #dados_json adicionado a produtos.
    produtos.append(produto_para_adicionar)
    return produto_para_adicionar, 201 #201 - Recurso criado

#Pesquisar produto por id.
#Definindo uma função
def procurar_por_id(id):
    # procurar em produtos por um id igual, para ao encontrar. 
    return next((p for p in produtos if p["id"] == id), None)

@app.route("/produto/<int:id>/buscar")
def get_produto_especifico(id):

    produto =  procurar_por_id(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404
    return {"produto encontrado": produto}


#atualizar um produto pelo id
@app.route("/produto/<int:id>/update", methods=["PUT"])
def update_produto(id):

    #pegar dados do JSON
    dados_json = request.json

    #dados obrigatórios
    obrigatorio = ["nome", "marca", "preco", "descricao"]
    for campo in obrigatorio:
        if campo not in dados_json:
            return {"erro": f"Dado faltando: {campo}"}, 400

    # procurar o produto pelo campo "id"
    produto = procurar_por_id(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404
    
    # atualizar produto
    produto.update(dados_json)

    return {"produto_atualizado": produto}, 200

@app.route("/produto/<int:id>/delete", methods=["DELETE"])
def deletar_produto(id):

    # procurar o produto pelo campo "id"
    produto = procurar_por_id(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404
    
    produtos.remove(produto)
    return {"produto": produto}