from typing import Optional

import fastapi
import pydantic

# Persistência / repositório

memoria_musicas = []


def persistencia_musica_salvar(nova_musica):
    codigo_nova_musica = len(memoria_musicas) + 1
    nova_musica['codigo'] = codigo_nova_musica
    memoria_musicas.append(nova_musica)
    return nova_musica


def persistencia_musica_pesquisar_todas():
    lista_musicas = list(memoria_musicas)
    return lista_musicas


def persistencia_pesquisar_pelo_codigo(codigo):
    musica_procurada = None
    for musica in memoria_musicas:
        if musica["codigo"] == codigo:
            musica_procurada = musica
            break
    return musica_procurada
# Regras / Casos de Uso / Buisiness Object


def regras_musicas_cadastrar(nova_musica):
    # TODO validar a nova música
    # regras
    nova_musica = persistencia_musica_salvar(nova_musica)
    return nova_musica


def regras_musica_pesquisar_todas():
    return persistencia_musica_pesquisar_todas()


def regras_musica_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo(codigo)


aplicacao_web = fastapi.FastAPI()


@aplicacao_web.get("/")
def rota_raiz():
    return {
        'ok': True,
        'versao': 'fase 1'
    }


class NovaMusica(pydantic.BaseModel):
    nome: str
    artista: str
    tempo: Optional[int]


@aplicacao_web.post("/musicas")
def rota_musica_cadastrar(nova_musica: NovaMusica):
    print('Registrando nova música', nova_musica.dict())
    nova_musica = regras_musicas_cadastrar(nova_musica.dict())
    return nova_musica


@aplicacao_web.get("/musicas")
def rota_musica_pesquisar_todas():
    return regras_musica_pesquisar_todas()


@aplicacao_web.get("/musicas/{codigo}")
def rota_musica_pesquisar_pelo_codigo(codigo: int):
    print("Consulta pelo código", codigo)
    return regras_musica_pesquisar_pelo_codigo(codigo)
