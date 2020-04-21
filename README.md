# Gerador de numeros da megasena

## Idéia
Baseado nos resultados anteriores, filtrado pelo mês e numero da semana, gera uma lista de números para jogar na megasena

## Para rodar:

A parte chata:
Não existe uma api que retorne todos os resultados da loteria, então encontrei um site que posso baixar os arquivos no formato do excel:
- https://asloterias.com.br/download-todos-resultados-mega-sena

Baixe, transforme o arquivo em csv (com o cabeçalho) e salve na pasta do programa com o nome `megasena.csv`

- `python3 extract-csv-splitted-by-month-year.py`
- `python3 generateNumbers.py <numero do mes> <numero da semana> `