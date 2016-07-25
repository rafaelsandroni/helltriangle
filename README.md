# Hell Triangle - Challenge

Dado um determinado triângulo, o algoritmo deve encontrar um caminho que resulte na soma máxima, percorrendo a lista de cima para baixo.

Sempre somando com os elementos da mesma coluna ou da próxima coluna à direita, da linha seguinte.

Exemplo:

6

3 4

5 6 7

A caminho da soma máxima é: 6 + 4 + 7 = 17
O número 4 ([i][col]) só pode ser somado com os números 6 ([i+1][Col]) ou 7 ([i+1][col+1]).

# Python

A escolha da linguagem Python foi feita seguindo os pontos: a possibilidade de codificação enxuta e rápida, facilidade de leitura e existência de módulo de testes unitários integrado à linguagem.

#Testing 

O arquivo compõe os testes unitários, escritos usando o unittest, módulo de testes padrão da liguagem python.

#Running

git clone https://github.com/rafaelsandroni/helltriangle.git

cd ./helltriangle

$ ./main.py

A lista (arr) contendo os elementos do triângulo, pode ser alterada em main.py.

#Result

========== results ==========
 triangle: [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]] 
 maximum total: 26
 path: [0, 1, 1, 2] 
 execution time: 0.000049s
=============================



