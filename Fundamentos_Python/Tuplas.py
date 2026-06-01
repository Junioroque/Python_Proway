# Tuplas

lista = ['Processado', 'Mouse', 'Teclado', 'Monitor', 'Placa Mãe'];
tupla = tuple('ABCD');
print(type(tupla));

print(tupla[1]);

print(tupla);

for x in range(0, len(tupla)):
    print(tupla[x]);
    
    
dia_semana = ('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab');
#print(dia_semana[2]);

print('-------------------------------------------');
# Faça um exercicio que o usuário informe o dia da 
# semana e retorne a posição em que se encontra do item.

print('[Dom | Seg | Ter | Qua | Qui | Sex | Sab]');
opcao = input("Informe o dia da semana desejado: ");
existe = False;

for x in range(0, len(dia_semana)):
    if(dia_semana[x].upper() == opcao.upper()):
        existe = True;

if(existe):
    print('Dia da semana está na posição ' + str(x));
else:
    print('Dia da semana inválido!');
        


    

