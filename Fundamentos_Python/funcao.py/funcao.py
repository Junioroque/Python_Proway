def escola(escola = 'Proway'):
    print('Você está estudando na escola '+ escola);

def SomaValores(valor_1, valor_2):
    print(valor_1 + valor_2);
    
def ValidarAcesso(usuario):
    # Vamos utiliar como padrão o usuário Proway
    if(usuario == "Proway"):
        print('Login efetuado com sucesso!');
        escola();
    else:
        print('Usuário inválido. Verifique a senha!');