Desafio dos OVNIs
=================

Dizem que por detrÃ¡s de cada cometa hÃ¡ um OVNI. Esses OVNIs tem por objetivo buscar bons desenvolvedores na Terra.

Infelizmente, sÃ³ hÃ¡ espaÃ§o suficiente para levar um grupo de desenvolvedores por vez. Afim de selecionÃ¡-los, hÃ¡ um engenhoso esquema, da associaÃ§Ã£o do nome do cometa ao nome do grupo, que possibilita a cada grupo saber se serÃ¡ levado ou nÃ£o.

Os dois nomes, do grupo e do cometa, sÃ£o convertidos em um nÃºmero que representa o produto das letras do nome, onde "A" Ã© 1 e "Z" Ã© 26. Assim, o grupo "LARANJA" seria 12 * 1* 18 * 1 * 14 * 10 * 1 = 30240. 

Se o resto da divisÃ£o do nÃºmero do grupo por 45 for igual ao resto da divisÃ£o do nÃºmero do cometa por 45, entÃ£o o grupo serÃ¡ levado.

Para os cometas e grupos abaixo, vocÃª deverÃ¡ desenvolvedor um programa ao qual dirÃ¡ o grupo que **nÃ£o** serÃ¡ levado?

| Cometa   | Grupo    |
|:--------:|:--------:|
| HALLEY	 | AMARELO  |
| ENCKE	   | VERMELHO |
| WOLF     | PRETO   |
| KUSHIDA	 | AZUL     |



### Resoluç

```
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
```

##Demonstrando resultado


![image](https://user-images.githubusercontent.com/116848225/218853571-60543fe9-cd1c-4384-b8ad-c69ae569080b.png)
