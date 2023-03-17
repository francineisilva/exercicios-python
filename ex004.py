#Toda vez que a variável não for do tipo string, você vai precisar declarar o tipo primitivo dela.

valor1 = int(input('Digite um valor: '))

valor2 = int(input('Digite outro valor: '))

soma = valor1 + valor2

print('A soma entre {} e {} é igual {}'.format(valor1, valor2, soma))