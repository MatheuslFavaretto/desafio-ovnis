def letras(nome):
    produto = 1
    for letra in nome:
        valor = ord(letra.upper()) - 64
        produto *= valor
    return produto

def verificar_grupo_levado(nome_grupo, nome_cometa):
    numero_grupo = letras(nome_grupo)
    numero_cometa = letras(nome_cometa)
    resto_grupo = numero_grupo % 45
    resto_cometa = numero_cometa % 45
    if resto_grupo == resto_cometa:
        print(f"O grupo {nome_grupo} não será levado pelo cometa {nome_cometa}.")
    else:
        print(f"O grupo {nome_grupo} será levado pelo cometa {nome_cometa}.")

nome_grupo = ['AMARELO', 'VERMELHO', 'PRETO', 'AZUL']
nome_cometa = ['HALLEY', 'ENCKE', 'WOLF', 'KUSHIDA']

for grupo in nome_grupo:
    for cometa in nome_cometa:
        verificar_grupo_levado(grupo, cometa)
