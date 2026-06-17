texto = list()
# arquivo = open('arquivo.txt', 'a');

# texto.append('Conteudo da primeira linha!');
# texto.append('\nConteudo da segunda linha!');
# texto.append('\nConteudo da terceira linha!');

# arquivo.writelines(texto);
# arquivo.close();

# # Abrir um arquivo para leitura
# arquivo = open('arquivo.txt', 'a');
# print(arquivo.read(50));
# print(arquivo.readlines());
# print(arquivo.readlines());
# print(arquivo.readlines());

print('' .ljust(35, '-'));

arquivo = open('arquivo.txt', 'r');
total = 0;

for linha in arquivo:
    # rsplit() - Retorna as informações em formato de lista
    # linha = linha.rsplit();
    # print(linha);

    # rstrip() = Retorna as informações no formato normal
    linha = linha.rstrip();
    print(linha);
    
    total += 1;
    
arquivo.close();
print('' .ljust(35, '-'));
print('Total de linhas: ', str(total));