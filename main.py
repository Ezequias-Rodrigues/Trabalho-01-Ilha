pontos = 100
escolha = 0
print("Você acorda em uma ilha deserta após um naufrágio." \
"\nO sol quente bate em sua pele, e o som das ondas quebra o silêncio." \
"\nSua última lembrança é do barco afundando durante uma tempestade." \
"\nAgora, você precisa tomar decisões para garantir sua sobrevivência")
print("\n")
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

if(escolha == '1'):
    print("Você entra na floresta e logo encontra um pequeno rio de água cristalina\n" \
    "A sombra das árvores oferece um alívio do calor intenso.\n")
    escolha = 0
    while (escolha == 0):
        escolha = input("Faça sua escolha: ")
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = 0
        print("\n")
    if(escolha == '1'):
        print("")

else:
    print("Você decide caminhar pela praia, sentindo o calor do sol e a areia quente sob seus pés.\n" \
    "Você também começa a sentir fome e cansaço.\n")
    while (escolha == 0):
        escolha = input("Faça sua escolha: ")
        if(not (escolha == "1" or escolha == "2")):
            print("Escolha inválida. Use 1 ou 2.")
            escolha = 0
        print("\n")