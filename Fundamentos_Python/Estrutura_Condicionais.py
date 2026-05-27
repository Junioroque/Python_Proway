numero_1 = int(input("Informe um valor inteiro: "));
numero_2 = int(input("Informe outro valor inteiro: "));

if( numero_1 == numero_2):
    print("Os valores informados são iguais.");
else:
     if(numero_1 > numero_2):
        print("O primeiro numero e maior que o segundo.");
     else:
        print("O segundo numero e maior que o primeiro.");

#Resumir a condição

if(numero_1 == numero_2):
    print("Numeros iguais.");
elif(numero_1 > numero_2):
    print("Primeiro numero e maior.");
else:
    print("O segundo numero e maior.");