soma = 0 #Declaro a variável soma como 0
numero = (2**1000) #Numero o qual quero somar os algaritimos
string = str(numero) #Transformo em str para poder usar posição. Ex: "b[1] = 2"

print("Número a ser somado: " + string) #Imprimo o numero a ser somado

for i in range(len(string)): #Crio um for com o range do tamanho da minha string
        soma += int(string[i]) #Pata cada indice da minha string (que é um numero) ele soma e armazena em soma

print("\nResultado Final : ",soma) #Printa o resultado final