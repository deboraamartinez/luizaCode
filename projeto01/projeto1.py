
from typing import List

import pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Classe representando os dados do cliente

class Usuario(pydantic.BaseModel):
    id: int
    nome: str
    email: str
    senha: str

# Classe representando os dados do endereço do cliente


class Endereco(pydantic.BaseModel):
    id: int
    id_usuario: int
    rua: str
    cep: str
    cidade: str
    estado: str

# Classe representando a lista de endereços de um cliente


class ListaDeEnderecosDoUsuario(pydantic.BaseModel):
    id_usuario: int
    enderecos: List[Endereco] = []


# Classe representando os dados do produto


class Produto(pydantic.BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float


# Classe representando o carrinho de compras de um cliente com uma lista de produtos


class CarrinhoDeCompras(BaseModel):
    id: int
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = []
db_produtos = []
db_end = []
db_carrinhos = []


def persistencia_salvar_usuario(usuario):
    codigo_usuario = len(db_usuarios) + 1
    usuario.id = codigo_usuario
    db_usuarios.append(usuario)
    return usuario


def persistencia_pesquisar_id(id, array):
    id_procurado = [x for x in array if x.id == id]
    return id_procurado


def persistencia_pesquisar_nome(nome, array):
    id_procurado = [x for x in array if x.nome == nome]
    return id_procurado


def persistencia_salvar_endereco(endereco, id_usuario):
    codigo_endereco = len(db_end) + 1
    endereco.id = codigo_endereco
    codigo_usuario = id_usuario
    endereco.id_usuario = codigo_usuario
    db_end.append(endereco)
    return endereco


def persistencia_pesquisar_enderecos(array, id_usuario):
    endereco_procurado = [x for x in array if x.id_usuario == id_usuario]
    return endereco_procurado


def persistencia_salvar_produto(produto):
    codigo_produto = len(db_produtos) + 1
    produto.id = codigo_produto
    db_produtos.append(produto)
    return produto


def persistencia_salvar_carrinho(carrinho, id_usuario):
    codigo_carrinho = len(db_carrinhos)
    codigo_carrinho = len(db_carrinhos) + 1
    carrinho.id = codigo_carrinho
    codigo_usuario = id_usuario
    carrinho.id_usuario = codigo_usuario
    db_carrinhos.append(carrinho)
    return carrinho


def persistencia_pesquisar_carrinho(array, id_usuario):
    carrinho_procurado = [x for x in array if x.id_usuario == id_usuario]
    return carrinho_procurado


def persistencia_salvar_produto_carrinho(id_produto):
    produto_procurado = persistencia_pesquisar_id(db_produtos, id_produto)
    db_carrinhos.carrinho.id_produtos.append(produto_procurado)
    return

# REGRAS


def regras_usuario_cadastrar(usuario):
    usuario = persistencia_salvar_usuario(usuario)
    return usuario


def regras_endereco_cadastrar(endereco, id_usuario):
    endereco = persistencia_salvar_endereco(endereco, id_usuario)
    return endereco


def regras_produto_cadastrar(produto):
    produto = persistencia_salvar_produto(produto)
    return produto


def regras_carrinho_cadastrar(carrinho, id_usuario):
    carrinho = persistencia_salvar_carrinho(carrinho, id_usuario)
    return carrinho


@ app.post("/usuario/")
def criar_usuário(usuario: Usuario):
    novo_usuario = regras_usuario_cadastrar(usuario)
    return novo_usuario


@ app.get("/usuario/{id}")
def retornar_usuario(id: int):
    id_procurado = persistencia_pesquisar_id(id, db_usuarios)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    return id_procurado[0]


@ app.delete("/usuario/{id}")
def deletar_usuario(id: int):
    id_procurado = persistencia_pesquisar_id(id, db_usuarios)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    else:
        db_usuarios.remove(id_procurado[0])
        raise HTTPException(status_code=200, detail="OK")


@ app.get("/usuario/nome/{nome}")
def retornar_usuario_com_nome(nome: str):
    nome_procurado = persistencia_pesquisar_nome(nome, db_usuarios)
    if len(nome_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    return nome_procurado[0]


@ app.post("/endereco/{id_usuario}")
def criar_endereco(endereco: Endereco, id_usuario: int):
    id_procurado = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    novo_endereco = regras_endereco_cadastrar(endereco, id_usuario)
    return novo_endereco


@ app.get("/usuario/{id_usuario}/endereco/")
def pesquisar_endereco(id_usuario: int):
    id_procurado = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    endereco_procurado = persistencia_pesquisar_enderecos(db_end, id_usuario)
    if len(endereco_procurado) == 0:
        return []
    return endereco_procurado


@ app.delete("/endereco/{id}")
def deletar_endereco(id: int):
    id_procurado = persistencia_pesquisar_id(id, db_end)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    else:
        db_end.remove(id_procurado[0])
        raise HTTPException(status_code=200, detail="OK")


@ app.post("/produto/")
def criar_produto(produto: Produto):
    novo_produto = regras_produto_cadastrar(produto)
    return novo_produto


@ app.get("/produto/{id}")
def criar_produto(id: int):
    id_procurado = persistencia_pesquisar_id(id, db_produtos)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    return id_procurado[0]


@ app.delete("/produto/{id}")
def deletar_produto(id: int):
    id_procurado = persistencia_pesquisar_id(id, db_produtos)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    else:
        db_produtos.remove(id_procurado[0])
        raise HTTPException(status_code=200, detail="OK")


@ app.post("/carrinho/{id_usuario}")
def criar_carrinho(carrinho: CarrinhoDeCompras, id_usuario: int):
    id_usuario = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_usuario) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    novo_carrinho = regras_endereco_cadastrar(carrinho, id_usuario)
    return novo_carrinho


@ app.post("/carrinho/{id_usuario}/{id_produto}")
def criar_carrinho(carrinho: CarrinhoDeCompras, id_usuario: int, id_produto: int):
    id_usuario = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_usuario) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    id_produto_procurado = persistencia_pesquisar_id(id_produto, db_produtos)
    if len(id_produto_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    carrinho_procurado = persistencia_pesquisar_carrinho(
        db_carrinhos, id_usuario)
    if len(carrinho_procurado) == 0:
        novo_carrinho = regras_carrinho_cadastrar(carrinho, id_usuario)
        novo_carrinho.id_produtos.append(id_produto_procurado[0])
        return novo_carrinho
    else:
        adicionando_produto = carrinho_procurado[0].id_produtos.append(
            id_produto_procurado[0])
        return carrinho_procurado[0]


@app.delete("/carrinho/{id_usuario}")
def apagar_carrinho(id_usuario: int):
    id_procurado = persistencia_pesquisar_id(id_usuario, db_carrinhos)
    if len(id_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    else:
        db_carrinhos.remove(id_procurado[0])
        raise HTTPException(status_code=200, detail="OK")


@ app.delete("/carrinho/{id_usuario}/{id_produto}")
def apagar_produto_carrinho(id_usuario: int, id_produto: int):
    id_usuario = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_usuario) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    id_produto_procurado = persistencia_pesquisar_id(id_produto, db_produtos)
    if len(id_produto_procurado) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    carrinho_procurado = persistencia_pesquisar_carrinho(
        db_carrinhos, id_usuario)
    removendo_produto = carrinho_procurado[0].id_produtos.remove(
        id_produto_procurado[0])
    return carrinho_procurado[0]


@app.get("/carrinho/{id_usuario}")
def pegar_carrinho_total(id_usuario: int):
    id_usuario = persistencia_pesquisar_id(id_usuario, db_usuarios)
    if len(id_usuario) == 0:
        raise HTTPException(status_code=404, detail="FALHA")
    carrinho_procurado = persistencia_pesquisar_carrinho(
        db_carrinhos, id_usuario)
    contando_produtos = len(carrinho_procurado[0].id_produtos)
    carrinho_procurado[0].quantidade_de_produtos = contando_produtos
    soma_total = 0
    for id_produtos in carrinho_procurado[0].id_produtos:
        soma_total += id_produtos.preco
    carrinho_procurado[0].preco_total = soma_total
    return carrinho_procurado[0]


@ app.get("/")
async def bem_vinda():
    site = "Seja bem vinda ao Carrinho do Magalu"
    return site.replace('\n', '')
