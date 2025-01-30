#List Comprehension
#Uma sintaxe mais curta para criar uma lista baseado em uma lista já existente
#Sintaxe: novaLista = [expressão for item in interable if condition == True]

#animais = ["cachorro", "gato", "tartaruga", "girafa"]
#novaLista = []

#for animal in animais:
#    if "t" in animal:
#        novaLista.append(animal)
#print(novaLista)

#novaLista = [animal for animal in animais if "t" in animal]
#print(novaLista)

#novaLista = [numero for numero in range(10) if numero%2 == 0]
#print(novaLista)

#animais = ["cachorro", "gato", "tartaruga", "girafa"]
#novaLista = [animal.upper() for animal in animais]
#print(novaLista)

animais = ["cachorro", "gato", "tartaruga", "girafa"]
novaLista = [animal if animal != "cachorro" else "macaco" for animal in animais]
print(novaLista)
