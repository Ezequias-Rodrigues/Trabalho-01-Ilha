import random
pontos = 100
escolha = 0
ultimo_dano = 0
print("Você acorda em uma ilha deserta após um naufrágio." \
"\nO sol quente bate em sua pele, e o som das ondas quebra o silêncio." \
"\nSua última lembrança é do barco afundando durante uma tempestade." \
"\nAgora, você precisa tomar decisões para garantir sua sobrevivência")
print("===== Escolhas: ===== ")
print("(1) Explorar a floresta em busca de recursos.")
print("(2) Caminhar pela praia e procurar sinais de vida.")
print("\n")
while (escolha == 0):
    
    escolha = input("Faça sua escolha: ")
    if(not (escolha == "1" or escolha == "2")):
        print("Escolha inválida. Use 1 ou 2.")
        escolha = 0
    print("\n")
ultimo_dano = random.randint(20 ,40)
pontos -= ultimo_dano
if(escolha == '1'):
    print("Você entra na floresta e logo encontra um pequeno rio de água cristalina\n" \
    "A sombra das árvores oferece um alívio do calor intenso.")
    print("Sua energia atual: ", pontos)
    print("\n")
    print("===== Escolhas: ===== ")
    print("(1) Beber a água do rio.")
    print("(2) Procurar uma outra fonte de água.")
    escolha = 0
    while (escolha == 0):
        escolha = input("Faça sua escolha: ")
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = 0
        print("\n")
    if(escolha == '1'):
        ultimo_dano = random.randint(15 ,35)
        pontos -= ultimo_dano
        primeira_vez = True
        while(escolha == '1'):
            
            if(primeira_vez):
                print("A água pode estar contaminada. Você começa a se sentir mal e perde", ultimo_dano, "de energia, o que deseja fazer?")
                print("Sua energia atual: ", pontos)
                primeira_vez = False
            else:
            
                ultimo_dano = random.randint(15 ,35)
                pontos -= ultimo_dano
                print("Humm, voce começou a passar mal e perdeu", ultimo_dano, "de energia, o que deseja fazer?")
                print("Sua energia atual: ", pontos)
            print("\n")
            print("===== Escolhas: ===== ")
            print("(1) Beber a água do rio.")
            print("(2) Procurar uma fonte de água mais segura.")
            escolha = input("Faça sua escolha: ")
            if(pontos <= 18): 
                if(pontos < 0): pontos = 0
                print("Apesar de querer beber mais água, você percebe que essa seria uma ideia tola tomar mais água daqui depois de passar mal tantas vezes.\n" \
                "Você decide que seria melhor procurar uma fonte de água mais segura.")
                escolha = "2"
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = '1'
        print("\n")
    if(escolha == "2"): #Sim, é um if não else ou elif, pois o loop dentro do if escolha == 1 o cenario de saida é o mesmo q o escolha == 2
        ultimo_dano = random.randint(5 ,15)
        pontos += ultimo_dano
        print("Você encontra um coqueiro e consegue beber água de coco, ganhando", ultimo_dano, "de energia.")
        print("Sua energia atual: ", pontos)
        input("Aperte ENTER para continuar")
        print("\n")

else:
    print("Você decide caminhar pela praia, sentindo o calor do sol e a areia quente sob seus pés.\n" \
    "Você também começa a sentir fome e cansaço.\n")
    print("\n")
    print("===== Escolhas: ===== ")
    print("(1) Caçar ou Pescar.")
    print("(2) Procurar Frutas.")
    escolha = 0
    while (escolha == 0):
        escolha = input("Faça sua escolha: ")
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = 0
        print("\n")
    if(escolha == "1"):
        ultimo_dano = random.randint(5 ,35)
        pontos -= ultimo_dano
        print("Você não consegue coletar nada de proteína e consome", ultimo_dano,"de energia")
        print("Sua energia atual: ", pontos)
        if(pontos <= 0):
            print("Apesar de todos seus esforços, e sua capacidade estratégica, a natureza foi mais forte, e você sucumbiu...")
            quit()
    else:
        ultimo_dano = random.randint(10 ,25)
        pontos += ultimo_dano
        print("Você encontra frutas e recupera ", ultimo_dano,"de energia")
        print("Sua energia atual: ", pontos)
print("O sol começa a se pôr, e a temperatura cai rapidamente.\n"\
      "O vento aumenta, e você sabe que precisa se preparar para a noite.\n" \
    "Após algum tempo, você encontra destroços do barco, incluindo madeira, cordas e pedaços de tecido.")
print("===== Escolhas: ===== ")
print("(1) Construir um abrigo.")
print("(2) Acender uma fogueira.")
print("\n")
escolha = 0
while (escolha == 0):
        escolha = input("Faça sua escolha: ")
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = 0
        print("\n")
if(escolha == "1"):
    ultimo_dano = random.randint(10 ,25)
    pontos -= ultimo_dano
    print("Você gasta", ultimo_dano, "de energia para construir o abrigo." \
    "\nPela manhã, pescadores da ilha o encontram e decidem ajudá-lo.")
    print("Sua energia atual: ", pontos)
    if(pontos <= 0):
        print("Apesar de todos seus esforços, e sua capacidade estratégica, a natureza foi mais forte, e você sucumbiu...")
        quit()
else:
    ultimo_dano = random.randint(5 ,15)
    pontos -= ultimo_dano
    print("Você acende a fogueira e gasta", ultimo_dano, " de energia.\n" \
    "Um navio distante vê a fumaça e envia uma equipe de resgate rapidamente.")
    print("Sua energia atual: ", pontos)
    if(pontos <= 0):
        print("Apesar de todos seus esforços, e sua capacidade estratégica, a natureza foi mais forte, e você sucumbiu...")
        exit()
print("\n")
input("Aperte ENTER para continuar")
print("\n")
if(pontos >= 70):
    print("O resgate chega e você está tão bem que dá até para dar autógrafos para os socorristas.\n"\
          "(Final Alegre – Você foi resgatado, e até parece que esteve em um spa por dias!)")
elif(pontos >= 30):
    print("O resgate chega, mas você está tão fraco que mal consegue fazer uma piada.\n"\
          "(Final Irônico – Você sobreviveu, mas está mais parecendo um zumbi do que um herói.)")
else:
    print("O resgate chega, mas ele mal consegue levantar e até acha que o socorro é só mais um pesadelo.\n"\
          "(Final Surreal – Você foi resgatado, mas vai precisar de muitos cafés para voltar à vida normal!)")