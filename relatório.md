## Relatório
Aqui será registrado o passo-a-passo do Trabalho 1 de Mineração de Dados!

### Pré-processamento
Nessa fase, foi primeiramente feita uma avaliação dos dados, para verificar quais seriam necessários para responder as perguntas do trabalho. Foi concluído que os dados necessários eram somente os **jogadores de cada partida** e o **resultado dela**. No entanto, era necessário colocar os dados em um formato mais legível, pois os nomes dos jogadores não estavam escritos em um formato padrão, e o resultado de uma partida poderia ser expresso como um valor binário, não sendo necessário strings para isso. Assim, foi feito o seguinte procedimento:
- Foram removidas as colunas de contador, e todas as outras, com exceção de ***Jogadore(a)s*** e ***Resultado***;
    - Para facilitar, essas colunas nem sequer foram lidas ao tratar o dataset
- Os valores de ***Resultado*** foram alterados para valores binários, com uma vitória correspondendo ao valor 1, e uma derrota ao 0;
    - **Ex.:** Ágatha, Marta, GANHOU -> Ágatha, Martha, 1
- Os nomes dos jogadores foram todos padronizados, corrigindo erros de corrupção nos dados, se tornando: **Romario, Roberto, Ágata, Marta, Bárbara, Shelda, Ronaldo** e **Alonso**.
    - Para a padronização, a leitura foi feita usando codificação `latin-1`, a fim de permitir a leitura de certos unicode 'estranhos' que apareciam nos dados
    - Os erros foram corrigidos a partir de um mapeamento entre o nome incorreto e sua versão correta. Os erros foram identificados manualmente, mas corrigidos por esse mapeamento.

Resultado final dos dados:
```
    Jogadore(a)s,Resultado
    "Romario, Roberto, Alonso",0
    "Alonso, Roberto, Ágata",0
    "Ágata, Ronaldo, Marta",1
    "Ágata, Marta, Bárbara",1
    "Bárbara, Roberto, Romario",0
```

*Como o Dataset é muito extenso, foram colocadas somente as primeiras 5 linhas, de exemplo.