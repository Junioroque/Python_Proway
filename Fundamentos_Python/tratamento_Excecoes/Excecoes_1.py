try: # try tente fazer esse comando.
    print(2/0);
    print('Tentativa de comando!');

# except: # caso haja um erro, faça isso.
#     if(ZeroDivisionError == 0): # se o erro for de divisão por zero, faça isso.
#        print('Não e possivel dividir por zero!');
#     else: # caso haja outro erro, faça isso.
#         print('Não e divisivel por letra!');
# Ou utilizando o except para tratar cada tipo de erro, como abaixo:    
        
except ZeroDivisionError: # caso haja um erro de divisão por zero, faça isso.
    print('Não e possivel dividir por zero!');
except NameError: # caso haja um erro de tipo, faça isso.
    print('Não e divisivel por letra!');