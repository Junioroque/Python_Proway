# Laço de repetição
# While
numero = 1;
while (numero <= 10):
    if(numero % 2 == 0):
        print("Par: " + str(numero));
    else:
        print("Impar: " + str(numero));
    
    numero+= 1;     
    
# for
valor = int(input("Informe o valor da tabuada: "));
for x in range(1, 11):
    print(f'{x} x {valor} = {x * valor}');