#Toda variável precisa ter um nome e um tipo, e esse tipo pode ser (int, float, str, bool)
#estrutura
#nome = tipo
#Observação: O sinal de = é chamado de recebe, por ser um operador de atribuição, você chama igual para este == quando tem dois sinais.
#Quando você for personalizar o seu texto, não importa se é aspas duplas "" ou aspas simples ''
#Vamos conhecer o que são máscaras {}, elas pode ser substituídas pela variável na hora de mostrar a informação.

nome = input('Qual é o seu nome? ')

print('Olá {}, é um prazer te conhecer!'.format(nome))


