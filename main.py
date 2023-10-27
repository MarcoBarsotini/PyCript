def criptografar(texto, chave):  #Define a nova classe

    TextoInserido = "" #Define essa variável como Nula

    for caractere in texto:
        if caractere.isalpha():

            maiuscula = caractere.isupper()
            caractere = caractere.lower()    #Define os tipos de inserção

            #Essas duas linhas, realizam a extração Unicode 
            codigo = ord(caractere)
            codigo_criptografado = ((codigo - 97 + chave) % 26) + 97


            #condição de inserção
            if maiuscula:
                TextoInserido += chr(codigo_criptografado).upper()
            else:
                TextoInserido += chr(codigo_criptografado)

        else:
            TextoInserido += caractere

    return TextoInserido


def descriptografar(texto, chave):   # Função para descriptografar o texto
    
    return criptografar(texto, -chave)

def main():

    mensagem = input("Digite a mensagem que voce deseja criptografar: ")   #Pelo amor de deus, isso vc sabe ne? :P
    chave = int(13)

    mensagem_criptografada = criptografar(mensagem, chave)  #Define a mensagem criptografada nessa variável
    
    print("--------------------------------------------------------------\n")
    print("Mensagem criptografada:", mensagem_criptografada)
    

    descriptografar_opcao = input("Deseja descriptografar a mensagem? (S/N): ")
    
    if descriptografar_opcao.upper() == 'S':

        chave_descriptografar = int(input("Digite a chave para descriptografar: \n"))

        mensagem_descriptografada = descriptografar(mensagem_criptografada, chave_descriptografar)

        print("--------------------Chave liberada-------------------- \n")
        print("Mensagem descriptografada:", mensagem_descriptografada, "\n")
        print("------------------------------------------------------")

    else:
        print("--------------------Fim--------------------")

if __name__ == "__main__":
    main()


#Código feito pelo Marcão, pika das galáxias :P