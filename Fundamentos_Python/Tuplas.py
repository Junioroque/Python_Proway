# Tuplas

lista = ['Processado', 'Mouse', 'Teclado', 'Monitor', 'Placa Mãe'];
tupla = tuple('ABCD');
print(type(tupla));

print(tupla[1]);

print(tupla);

for x in range(0, len(tupla)):
    print(tupla[x]);
    
    
dia_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado');
print(dia_semana[2]);

print('-------------------------');
print('Dias da Semana');

for x in range(0, len(dia_semana)):
    if(dia_semana[x] == "domingo"):
        print(str(x+1) +' Domingo');
    elif(dia_semana[x] == "segunda"):
        print(str(x+1) +' Segunda-feira');
    elif(dia_semana[x] == "terça"):
        print(str(x+1) +' Terça-feira');
    elif(dia_semana[x] == "quarta"):
        print(str(x+1) +' Quarta-feira');
    elif(dia_semana[x] == "quinta"):
        print(str(x+1) +' Quinta-feira');
    elif(dia_semana[x] == "sexta"):
        print(str(x+1) +' Sexta-feira');
    else:
        print(str(x+1) +'Sabado');
        
# Faça um exercicio que o usuário informe o dia da 
# semana e retorne a posição em que se encontra do item.

posicaoItem = input("Informe o dia da Semana: ");
    

