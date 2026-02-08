
#biblioteca 
#import time # importa biblioteca de tempo . permite usar o sleep(humaniza o bot parece que esta pensando )
#porem não usei neste projeto para não queimar etapas . 
#funções da biblioteca 

#def panda(msg)
    #print(msg)
#time.sleep(1,5) #pausa de 1,5 segundos

# projeto chatbot de nome Panda . boas vindas/cadastro e pergunta se deseja continuar a conversa 
print("🐼 Olá! Seja muito bem-vindo(a)! Eu sou o Panda, seu assistente virtual.")

print('É um prazer falar com você hoje!') #mostra mensagem 
print("Antes de começarmos, posso saber seu nome completo?")#mostra mensagem 
nome = input("Digite seu nome completo:")
print("Obrigado," , nome,"! Que nome bonito!") #mostra mensagem e contem variavel armazenada com nome 

print("Legal! Estou registrando suas informações com carinho 📝") #mostra mensagem 
print("Para finalizar o cadastro, qual foi sua nota mais recente?") #mostra mensagem 

nota= float(input("sua nota:")) # variavel nota do tipo float para guardar valores com virgula; decimal . 

print("Você digitou,",nota,) #mostra mensagem e contem variavel nome 

print("Deixa eu analisar seus dados rapidinho...") #mostra mensagem 

print("Pronto! Já calculei seu resultado.")#mostra mensagem 

if nota >=7 : #condicional 
    print("Parabéns! Você foi APROVADO! 🎉 Continue assim!") #mostra mensagem a depender da nota digitada 
else : #condicional 
    print("Poxa, desta vez você foi REPROVADO, mas não desanime — você consegue melhorar!")#mostra mensagem a depender da nota digitada 