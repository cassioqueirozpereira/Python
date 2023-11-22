# tratando uma api

# dados
usuario = {
    "nome": "João",
    "redes": [{
        "nome": "facebook",
        "imagem_profile": "",
        "imagem_capa": "img_capa_1"
    }, {
        "nome": "twitter",
        "imagem_profile": "img_profile_2",
        "imagem_capa": ""
    }]
}

# método menos simplificado
print("\n\nMétodo menos simplificado\n")

# retorna a imagem do profile

def get_imagem_profile(usuario):
    for rede in usuario["redes"]:
        if rede["imagem_profile"]:
            return rede["imagem_profile"]
    
    return "default"

# retorna a imagem da capa

def get_imagem_capa(usuario):
    for rede in usuario["redes"]:
        if rede["imagem_capa"]:
            return rede["imagem_capa"]
    
    return "default"

print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario))


# utilizando partial
print("\n\nUtilizando partial\n")
from functools import partial

def get_imagem(qual_imagem, usuario):
    for rede in usuario["redes"]:
        if rede[qual_imagem]:
            return rede[qual_imagem]
    
    return "default"

get_profile = partial(get_imagem, "imagem_profile")
get_capa = partial(get_imagem, "imagem_capa")

print(get_profile(usuario))
print(get_capa(usuario))