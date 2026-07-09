# Entrada do nome do arquivo via stdin
arquivo_nome = input().strip()

# TODO: Inicialize as variáveis para armazenar o maior valor de pressão e o nome correspondente
maior_pressao = -1
paciente = ""

try:
    with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            if len(partes) != 2:
                continue  # Ignora linhas mal formatadas
            nome, pressao_str = partes
            try:
                pressao = int(pressao_str)
                if pressao > 0:
                    # TODO: Atualize as variáveis se encontrar uma pressão maior
                   maior_pressao = pressao
                   paciente = nome.strip()
            except ValueError:
                continue  # Ignora se a pressão não for um inteiro válido
except FileNotFoundError:
    print("Nenhum dado")
    exit()

# Imprima o resultado conforme especificado
if paciente is None:
    print("Nenhum dado")
# DICA: Se não houver paciente válido, imprima "Nenhum dado"
else:
    print(f"{paciente} {maior_pressao}")