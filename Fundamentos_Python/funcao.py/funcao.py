def escola(escola = 'Proway'):
    print('Você está estudando na escola '+ escola);

#def SomaValores(valor_1, valor_2):
#    print(valor_1 + valor_2);
 
produtos = [];
nome = '';
novoNome = '';

    
def ValidarAcesso(usuario, senha):
    # Vamos utiliar como padrão o usuário aluno = / senha = Proway
    if((usuario == "aluno") and (senha == "Proway")):
        print('Login efetuado com sucesso!');
        print("");
    else:
        print('Usuário inválido. Verifique a senha!');
        
def MostraMenuPrincipal():
    opcao = 0;
    
    while(opcao != 5):
        print('+'.ljust(31, '-')+'+');
        print('| 1- Cadastrar | 4- Visualizar |');
        print('| 2- Alterar   | 5- Sair       |');
        print('| 3- Excluir                   |');
        print('+'.ljust(31, '-')+'+');
        opcao = int(input('Informe a opção desejada: '));
        
        if(opcao == 1):
            # Cadasttrar
            print('Cadastrando...');
            nome = input("Nome do produto: ");
            if(nome in produtos):
                print(nome, ' já está casastrado!');
            else:
                produtos.append(nome);
                print(nome, ' cadastrado com sucesso!');
        elif(opcao == 2):
            # Alterar
            nome = input('Nome do produto que deseja alterar: ');
            if(nome in produtos):
                for x in range(0, len(produtos)):
                    if(produtos[x] == nome):
                        novoNome = input(f'{nome}, informe o novo nome do produto: ');
                        produtos[x] = novoNome;
                        print(nome, ' alterado para ', novoNome);
                        break;
                    else:
                        print('Produto não encontrado.');
            print('Alterando...');
        elif(opcao == 3):
            # Excluir
            nome = input('Informe o produto que desja excluir: ');
            if(nome in produtos):
                produtos.remove(nome);
                print(nome, ' excluido com sucesso!');
            else: 
                print(nome, ' não está cadastrado!');
        elif(opcao == 4):
            # Visualizar
            print(produtos);
        elif(opcao == 5):
            print('Obrigado por utilizar o nosso sistema...');
        else:
            print('Opção inválida. Informe uma opção válida!');