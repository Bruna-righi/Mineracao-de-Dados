# Carregar pacotes
library(arules)

# Carregar o dataset
df <- read.csv("Documentos/Mineração/Mineracao-de-Dados/partidas_limpo.csv",
               stringsAsFactors = FALSE)

# Preparar as transações
transacoes_list <- lapply(1:nrow(df), function(i) {
  jogadores <- unlist(strsplit(df[i, "Jogadore.a.s"], ",\\s*"))  # separar jogadores
  resultado <- df[i, "Resultado"]                                 # pega o valor da coluna resultado
  c(jogadores, resultado) 
})

# Converter lista de vetores em objeto transactions
transacoes <- as(transacoes_list, "transactions")

# Aplicar o algoritmo Apriori
# Parâmetros: suporte mínimo 10%, confiança mínima 50%
regras <- apriori(
  transacoes,
  parameter = list(supp = 0.1, conf = 0.5, target = "rules")
)

# Filtrar regras vencedoras
regras_vencedoras <- subset(regras, rhs %in% "Ganhou")

# Ordenar pelas regras mais confiáveis
regras_vencedoras <- sort(regras_vencedoras, by = "confidence", decreasing = TRUE)

cat("\n--- Combinações mais prováveis de vencer ---\n")
inspect(regras_vencedoras)

# Filtrar regras perdedoras
regras_perdedoras <- subset(regras, rhs %in% "Perdeu")

# Ordenar pelas regras mais confiáveis
regras_perdedoras <- sort(regras_perdedoras, by = "confidence", decreasing = TRUE)

cat("\n--- Combinações mais prováveis de perder ---\n")
inspect(regras_perdedoras)