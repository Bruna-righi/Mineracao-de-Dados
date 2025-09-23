## Relatório
Aqui será registrado o passo-a-passo do Trabalho 1 de Mineração de Dados!

### Pré-processamento (Arquivo `preproc.py`)
Nessa fase, foi primeiramente feita uma avaliação dos dados, para verificar quais seriam necessários para responder as perguntas do trabalho. Foi concluído que os dados necessários eram somente os **jogadores de cada partida** e o **resultado dela**. No entanto, era necessário colocar os dados em um formato mais legível, pois os nomes dos jogadores e o resultado das partidas não estavam escritos em um formato padrão. Assim, foi feito o seguinte procedimento:
- Foram removidas as colunas de contador, e todas as outras, com exceção de ***Jogadore(a)s*** e ***Resultado***;
    - Para facilitar, essas colunas nem sequer foram lidas ao tratar o dataset
- Os valores de ***Resultado*** foram padronizados para **Ganhou** e **Perdeu**;
- Os nomes dos jogadores também foram ajustados, corrigindo erros de corrupção nos dados, se tornando: **Romario, Roberto, Ágata, Marta, Bárbara, Shelda, Ronaldo** e **Alonso**.
- Em cada linha, os nomes dos jogadores foram organizados alfabéticamente
    - Para a padronização, a leitura foi feita usando codificação `latin-1`, a fim de permitir a leitura de certos unicode 'estranhos' que apareciam nos dados
    - Os erros foram corrigidos a partir de um mapeamento entre o nome incorreto e sua versão correta. Os erros foram identificados manualmente, mas corrigidos por esse mapeamento.

Resultado final dos dados:
```
    Jogadore(a)s,Resultado
    "Alonso, Roberto, Romario",Perdeu
    "Agata, Alonso, Roberto",Perdeu
    "Agata, Marta, Ronaldo",Ganhou
    "Agata, Barbara, Marta",Ganhou
    "Barbara, Roberto, Romario",Perdeu
```

*Como o Dataset é muito extenso, foram colocadas somente as primeiras 5 linhas, de exemplo.

### 
### Regras de Associação (Arquivo `verifica_assoc.R`)
Após o pré-processamento, aplicamos Mineração de Regras de Associação com o objetivo de descobrir:
- Combinações de jogadores mais associada a vitórias (lado direito da regra = `Ganhou`)
- Combinações de jogadores mais associada a derrotas (lado direito = `Perdeu`)
- Evidências de um possível "jogador estrela" (aquele cuja presença aumenta a probabilidade de vitória acima da taxa base do conjunto de dados)

#### Preparação dos dados para transações
Cada linha do arquivo `partidas_limpo.csv` foi transformada em uma transação contendo:
- Os nomes (já padronizados e ordenados) dos jogadores que participaram da partida
- O resultado da partida (`Ganhou` ou `Perdeu`)

Assim, o algoritmo pode gerar regras do tipo:
`{Jogador A, Jogador B}  =>  {Ganhou}`
ou
`{Jogador X}  =>  {Perdeu}`

#### Algoritmo utilizado
Foi usado o algoritmo `Apriori` (pacote `arules` em R) com parâmetros:
- `support >= 0.10` (a combinação aparece em pelo menos 10% das transações)
- `confidence >= 0.50` (pelo menos 50% das vezes em que o antecedente ocorre, o consequente também ocorre)
- `target = "rules"`

Após gerar as regras, elas foram filtradas em dois subconjuntos:
1. Regras com consequente `Ganhou` (potencialmente indicam sinergias vencedoras)
2. Regras com consequente `Perdeu` (indicam combinações que tendem a perder)

Ambos os conjuntos foram ordenados por `confidence` de forma decrescente para destacar as associações mais fortes dentro dos parâmetros definidos.

#### Combinação vitoriosa e jogador estrela
Após a aplicação do algoritmo para gerar as rgras com consequente `Ganhou` obtivemos o seguinte resultado:
```
        lhs                 rhs      support   confidence coverage  lift      count
    [1] {Agata, Marta}   => {Ganhou} 0.1266667 0.7037037  0.1800000 1.3708514 19   
    [2] {Barbara, Marta} => {Ganhou} 0.1133333 0.6800000  0.1666667 1.3246753 17   
    [3] {Marta}          => {Ganhou} 0.2866667 0.6718750  0.4266667 1.3088474 43   
    [4] {Agata}          => {Ganhou} 0.2266667 0.5483871  0.4133333 1.0682866 34   
    [5] {}               => {Ganhou} 0.5133333 0.5133333  1.0000000 1.0000000 77   
    [6] {Ronaldo}        => {Ganhou} 0.1400000 0.5121951  0.2733333 0.9977827 21   
```
Desse modo, foi possível constatar que:
- A combinação de jogadores mais associada a vitórias foi **Ágata e Marta** com uma confiança de aproximadamente 70%. 
- A jogadora estrela foi **Marta** com uma confiança de aproximadamente 67%

#### Combinação perdedora
Após a aplicação do algoritmo para gerar as rgras com consequente `Perdeu` obtivemos o seguinte resultado:
```
        lhs                   rhs      support   confidence coverage  lift     count
    [1] {Shelda}           => {Perdeu} 0.1333333 0.6250000  0.2133333 1.284247 20   
    [2] {Barbara, Roberto} => {Perdeu} 0.1200000 0.5454545  0.2200000 1.120797 18   
    [3] {Romario}          => {Perdeu} 0.1466667 0.5238095  0.2800000 1.076321 22   
    [4] {Roberto}          => {Perdeu} 0.2266667 0.5230769  0.4333333 1.074816 34   
    [5] {Barbara}          => {Perdeu} 0.2000000 0.5084746  0.3933333 1.044811 30 
```
Desse modo, foi possível constatar que:
- A combinação de jogadores mais associada a derrotas foi **Barbara, Roberto** com uma confiança de aproximadamente 55%. 