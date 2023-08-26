### Coletando informações ###

# Solicitar ao usuário o nome
nome = str(input("Qual o seu nome? "))

# Opções de pronomes e gêneros
pronomes = ["Femininos", "Masculinos", "Neutros"]
generos = {
    "Femininos": ["Mulher Cis", "Mulher Trans", "Travesti"],
    "Masculinos": ["Homem Cis", "Homem Trans"],
    "Neutros": ["Não Binárie"]
}

print(f"Muito prazer, {nome}. Quais são os seus pronomes?") # Usando f-strings para formatar strings de maneira conveniente.
for i, pronome in enumerate(pronomes):
    print(f"{i+1}. {pronome}")

# "for i, pronome in enumerate(pronomes):"
# "for" para percorrer a lista de pronomes ('pronomes').
#  Enumerate é uma função que retorna um índice ('i') e o valor ('pronome') de cada item na lista.

# "print(f"{i+1}. {pronome}")
# Dentro do loop, essa linha exibe cada opção de pronome junto com um número.
# A expressão {i+1} é usada para exibir o número da opção (começando em 1, em vez de 0, porque índices de listas são baseados em 0).

escolha_pronome = int(input())
pronome_escolhido = pronomes[escolha_pronome - 1]

print("E qual o seu gênero?")
for i, genero_opcao in enumerate(generos[pronome_escolhido]):
    print(f"{i+1}. {genero_opcao}")

escolha_genero = int(input())
genero_escolhido = generos[pronome_escolhido][escolha_genero - 1]


### Significado e História do Nome ###

import requests
import urllib.parse

def obter_significado_e_historia(nome):
    nome_codificado = urllib.parse.quote(nome)  # Codifica o nome para ser seguro na URL
    url = f"https://www.behindthename.com/api/lookup.json?name={nome_codificado}&key=na335737816"

    response = requests.get(url)
    data = response.json()

    if data and isinstance(data, list) and len(data) > 0:
        significado = data[0].get("meaning")
        historia = data[0].get("history")
        return significado, historia
    else:
        return None, None
    
significado_nome, historia_nome = obter_significado_e_historia(nome)

### Exibindo Resultados ###


if significado_nome and historia_nome:
    print(f"Sabia que {nome} significa: {significado_nome}")
    print(f"E que a história de {nome} é: {historia_nome}")
else:
    print(f"Desculpe, não consegui encontrar informações sobre o seu nome, {nome}. Mas tenho certeza de que tem um significado lindo.\n")

print("Lembre-se, todos os seres são únicos, complexos e digno de afeto.")