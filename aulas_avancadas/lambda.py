#uma função lambda é uma pequena função anônima
#recebe os argumentos porem só pode executar uma expressão
# lambda argumentos : expressão

x = lambda a:a*3
print(x(4))

soma = lambda a,b:a+b
print(soma(7,7))

graus_celsius = lambda f:(5/9)*(f-32)
print(graus_celsius(32))
