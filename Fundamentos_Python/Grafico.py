import matplotlib.pyplot as grafico

notas = [8, 7, 6, 10]
bimestre = ['1º Bimestre', '2º Bimestre', '3º Bimestre', '4º Bimestre']

grafico.title('Notas do Bimestrais');
grafico.plot(bimestre, notas);
grafico.show();