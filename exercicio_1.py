"""
#### Exercício 1

Receba um número e calcule o fatorial dele.

Obs: O fatorial de um número é calculado pela seguinte fórmula "n! = n · (n-1) · (n-2) … 3 · 2 · 1". Ou seja, por exemplo:

4! = 4 * 3 * 2 * 1 = 24.

Exemplo:

Digite um número:
4

O fatorial de 4 é 24.
--------
Digite um número:
5

O fatorial de 5 é 120.

Dica: Para ajudar nesse cálculo, lembre-se das estruturas de repetição. 

Pode-se utilizar o comando "while" ou até o "for" para te ajudar nisso.

Fonte: Curso em vídeo.
"""
# Receba um número do usuário
numero = int(input("Digite um número:\n"))

# Inicializa a variável fatorial com 1
fatorial = 1

# Calcula o fatorial usando um laço for
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")
