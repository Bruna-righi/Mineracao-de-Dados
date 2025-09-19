import pandas as pd

df = pd.read_csv("_ASSOC_FuteVoleiStars.csv", usecols=["Jogadore(a)s", "Resultado"], encoding='latin-1')

df["Resultado"] = df["Resultado"].str.upper().map({"GANHOU":"Ganhou", "PERDEU":"Perdeu"})

df = df.replace({u"\u00A0": ""}, regex=True)

correcoes = {
    "romario": "Romario",
    "Romario": "Romario",
    "roberto": "Roberto",
    "Rob'erto": "Roberto",
    "Agata": "Agata",
    "?gata": "Agata",
    "Barbara": "Barbara",
    "Brbara" : "Barbara",
    "shelda" : "Shelda"
}
def limpar_nome(nome):
    if not isinstance(nome, str):
        return None
    nome = nome.strip()
    return correcoes.get(nome, nome)  

# Aplica a limpeza em cada jogador da lista e ordena alfabeticamente
df["Jogadore(a)s"] = df["Jogadore(a)s"].apply(
    lambda x: ", ".join(sorted([limpar_nome(n) for n in str(x).split(",")]))
)

df.to_csv("partidas_limpo.csv", index=False)