try:
    # arquivo = open('teste_01.txt', 'r');
    # arquivo.close();
    
    arq = open('aquivo2.txt', 'w');
    arq.write('Carlos, 150\n');
    arq.write('Maria, 120\n');
    arq.write('Jose, 110\n');
    arq.close();
    
    y = 1;
    print(y/x);
    
except ZeroDivisionError as mensagem:
    print('Impossivel dividir por zero! [' + str(mensagem) + ']');
except NameError as mensagem:
    print('Variavel não declarada. [' + str(mensagem) + ']');
except FileNotFoundError:
    print('Arquivo inexitente.');
    