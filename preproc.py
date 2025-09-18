import pandas as pd
import unidecode

df = pd.read_csv("_ASSOC_FuteVoleiStars.csv", usecols=["Jogadore(a)s", "Resultado"], encoding='latin-1')

df["Resultado"] = df["Resultado"].str.upper().map({"GANHOU":1, "PERDEU":0})

df = df.replace({u"\u00A0": ""}, regex=True)

correcoes = {
    "romario": "Romario",
    "Romario": "Romario",
    "roberto": "Roberto",
    "Rob'erto": "Roberto",
    "Agata": "Ágata",
    "?gata": "Ágata",
    "Barbara": "Bárbara",
    "Brbara" : "Bárbara",
    "shelda" : "Shelda"
}
def limpar_nome(nome):
    if not isinstance(nome, str):
        return None
    nome = nome.strip()
    return correcoes.get(nome, nome)  

# Aplica a limpeza em cada jogador da lista
df["Jogadore(a)s"] = df["Jogadore(a)s"].apply(
    lambda x: ", ".join([limpar_nome(n) for n in str(x).split(",")])
)

df.to_csv("partidas_limpo.csv", index=False)