itens = []
print(type(itens));

itens = ['Mouse', 'Teclado', 'Monitor'];
print(itens);

print('------------------------');

print(itens[1]);

print('------------------------');

# Manipular lista
# Insert pode escolher a posição
itens.insert(0, 'CPU');
itens.insert(4, 'Placa Mãe');
print(itens);

# Append sempre insere na ultima lista
itens.append('Placa Video');
print(itens)


# Pop remove item da lista pode escolher a posição;
itens.pop(2);
print(itens);

# Remove o itens da lista pelo nome
itens.remove('Placa Video');
print(itens);