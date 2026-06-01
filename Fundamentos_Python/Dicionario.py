dicionario = {1, 2, 3};

#print(type(dicionario));

numero = {1 : 'one', 2 : 'two', 3 : 'three'};
#print(numero[3]);
valor = int(input("Digite uma posição que deseja: "));

if(numero.get(valor) == None):
    print("Posição inexistente!");
else:
    print(numero.get(valor));
 
print('---------------------------');
   
# Adicionar uma nova chave

print(numero);
print('');
numero[4] = 'four';
print(numero);

indice = int(input('Qual posição deseja excluir? '));
print(numero.pop(indice, 'Posição Inexistente!'));

print(numero);

numero_2 = {7 : 'seven', 8 : 'height'};

numero.update(numero_2);
print(numero)