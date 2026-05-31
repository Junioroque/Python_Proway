# Percorrer a lista, quantos itens tem
itens = ['Processador', 'Mouse', 'Teclado', 'Monitor', 'Placa Mãe'];
print(len(itens));

for x in range(0, len(itens)):
    print(itens[x]);
    
print('-------------------------');

existe = False;
produto = input('Qual item deseja excluir da lista? ');
for x in range(0,len(itens)):
    if (produto.upper() == itens[x].upper()):
        itens.pop(x);
        existe = True;
        break
    
print(itens);
if (existe):
    print(produto+ ' foi excluido da lista.');
else:
    print(produto + ' não existe na lista.');
    
# Ordenar lista e Reverse lista
print(itens);
print("Lista Ordenar: ");
itens.sort();
print(itens);
print("Lista Reverse: ")
itens.reverse();
print(itens);

# Tamanho da lisa
print("Tamanho da lista: ");
print(len(itens));