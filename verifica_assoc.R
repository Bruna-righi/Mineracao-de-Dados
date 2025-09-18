df = read.csv("C:\\Users\\bruna\\Desktop\\Coisas da Bruna\\estudos\\FACULDADE\\4° semestre\\Mineração de Dados\\partidas_limpo.csv")

transacoes_list <- apply(df, 1, function(x) {
  jogadores <- unlist(strsplit(x["Jogadore.a.s"], ",\\s*"))  # separa por vírgula
  c(jogadores, x["Resultado"])  # adiciona resultado como item
})

transacoes_list
transacoes <- as(transacoes_list, "transactions")

library(arules)

regras <- apriori(
  transacoes,
  parameter = list(supp = 0.1, conf = 0.6)
)

inspect(regras)