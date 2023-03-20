# SatisfacaoRestricao
EP 2 - Inteligência artificial 

### Adendos
O exercício foi originalmente feito no replit, o repositório no github foi feito posteriormente. Para testar, é recomendado o replit (https://replit.com/@fabsdk/EP2-IA-LABORATORIO#main.py).
Os tópicos 3 e 4 estão difíceis de entender uma vez que: A função de backtracking foi entregue pronta e em nenhum momento foi explicado em aula o que são as otimizações solicitadas. 

### Situação Problema: CSP - Uso das Equipamentos no Laboratório de Química do SENAC
Suponha que um laboratório de química precisa organizar o uso de seus equipamentos para garantir que todas as análises necessárias possam ser realizadas dentro do prazo esperado e que as restrições de segurança e capacidade dos equipamentos sejam cumpridas. O laboratório possui um conjunto de equipamentos, como balanças, espectrômetros e microscópios, que são usados para realizar diferentes tipos de análises químicas.

Existem várias análises que precisam ser realizadas, cada uma com seus próprios requisitos de equipamentos e tempo de execução. Alguns equipamentos só podem ser usados para uma análise específica, enquanto outros podem ser compartilhados entre diferentes análises.

As restrições a serem satisfeitas incluem:

1. Cada equipamento tem uma capacidade máxima de uso diário e só pode ser usado para uma análise por vez.
2. Uma análise não pode estar em 2 equipamentos ao mesmo tempo.
3. Cada análise fica 1 hora em cada equipamento

O objetivo é encontrar um cronograma de uso de equipamentos que atenda a todas as restrições e minimize o tempo total necessário para concluir todas as análises.

Para ajudar a visualizar o problema, aqui está uma tabela com as análises, os equipamentos necessários e os tempos de execução estimados:

**Tabela de Análises**

| Análise | Equipamentos Necessários |
| --- | --- |
| Análise 1 | Espectrofotômetro UV-VIS, Cromatógrafo Gasoso |
| Análise 2 | Cromatógrafo Líquido, Espectrômetro Infravermelho |
| Análise 3 | Microscópio, Balança Analítica |
| Análise 4 | Espectrômetro de Massa |
| Análise 5 | Agitador Magnético, Espectrômetro Infravermelho |
| Análise 6 | Cromatógrafo Líquido, Espectrofotômetro UV-VIS |
| Análise 7 | Espectrofotômetro UV-VIS, Microscópio |
| Análise 8 | Cromatógrafo Gasoso |
| Análise 9 | Espectrômetro Infravermelho, Balança Analítica |
| Análise 10 | Espectrômetro de Massa, Cromatógrafo Gasoso |

**Tabela de Restrições**

| Equipamento | Tempo Máximo de Uso por Dia |
| --- | --- |
| Balança Analítica | 6 horas |
| Agitador Magnético | 4 horas |
| Cromatógrafo Líquido | 8 horas |
| Cromatógrafo Gasoso | 6 horas |
| Espectrofotômetro UV-VIS | 4 horas |
| Espectrômetro Infravermelho | 6 horas |
| Espectrômetro de Massa | 4 horas |
| Microscópio | 6 horas |

Deve-se gerar um plano de uso de cada equipamento na semana para que todas as análises sejam concluídas

### Representação e modelagem
Criamos uma tabela e separa por equipamento e tempo máximo de uso por dia;
Cada analise é alocada em um determinado horário.
Para as variáveis temos: analises e equipamentos
Para os domínios temos: horários possíveis para serem feitas as analises nos equipamentos.

### Exibição de dados
```
Olá usuário, seja-bem vindo ao Laboratório de Química do SENAC :)

Aqui estão os hórarios em quais os equipamentos podem ser útilizados para análise

Horário 1: A1-EUV
Horário 2: A1-CG
Horário 1: A2-CL
Horário 2: A2-EI
Horário 1: A3-MC
Horário 2: A3-BA
Horário 1: A4-EM
Horário 1: A5-AM
Horário 3: A5-EI
Horário 2: A6-CL
Horário 3: A6-EUV
Horário 2: A7-EUV
Horário 3: A7-MC
Horário 1: A8-CG
Horário 1: A9-EI
Horário 3: A9-BA
Horário 2: A10-EM
Horário 3: A10-CG
```
