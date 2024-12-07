print("*Que página de meme do Instagram você é?*")
 
idade = int(input("Qual a sua idade?\n"))
print(idade)
 
if 0 <= idade < 25:
	tempo_de_video = int(input("Quantos segundos são necessários para saber se um vídeo é bom?\n"))
	print(tempo_de_video)
	if 0 <= tempo_de_video <= 5:
		print("RESULTADO")
		print("Você deveria estar no TikTok")
	elif tempo_de_video > 5:
		print("RESULTADO")
		print("Sua página de memes é: @meltmemes")
	else:
		print("Erro: entrada inválida")
 
elif 25 <= idade <= 40:
	banda_favorita = input("Qual banda você gosta mais?\n")
	if banda_favorita == "A" or banda_favorita == "B":
		if banda_favorita == "A":
			print("A) Matanza")
		elif banda_favorita == "B":
			print("B) Iron Maiden")
		print("RESULTADO")
		print("Sua página de memes é: @badrockistamemes")
	elif banda_favorita == "C" or banda_favorita == "D":
		if banda_favorita == "C":
			print("C) Imagine Dragons")
		elif banda_favorita == "D":
			print("D) BlackPink")
		sim_ou_nao = input("São as capivaras os melhores animais da Terra?\n")
		print(sim_ou_nao)
		if sim_ou_nao == "Sim":
			print("RESULTADO")
			print("Sua página de memes é: @genteboamemes")
		elif sim_ou_nao == "Não":
				print("RESULTADO")
				print("Sua página de memes é: @wrongchoicememes")
		else:
			print("Erro: entrada inválida")
 
elif 40 < idade <= 125:
	imagem_de_bom_dia = input("Que imagem de bom dia você manda no grupo da família?\n")
	if imagem_de_bom_dia == "A":
		print("A) Bebê em roupa de flor")
		print("RESULTADO")
		print("Sua página de memes é: @bomdiabebe")
	elif imagem_de_bom_dia == "B":
		print("B) Gato")
		print("RESULTADO")
		print("Sua página de memes é: @kittykatmsgs")
	elif imagem_de_bom_dia == "C":
		print("C) Coração e rosas")
		print("RESULTADO")
		print("Sua página de memes é: @bomdiaflordodia")
	else:
		print(imagem_de_bom_dia)
		print("Erro: entrada inválida")
 
else:
	print("Erro: entrada inválida")