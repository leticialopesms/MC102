dia_do_mês = int(input()) 
dia_da_semana = input() 
valor_inicial = float(input()) 
  
if dia_do_mês % 7 == 0: 
    v = valor_inicial / 2 
else: 
    if dia_da_semana == "sexta-feira": 
        v = 0.75 * valor_inicial 
    else: 
        if valor_inicial > dia_do_mês: 
            v = valor_inicial - dia_do_mês 
        else: 
            v = 0.00 
  
print(f"{v:.2f}") 
# Aqui utilizei um comando ainda não visto em sala, pois meus
# números inteiros de saída não estavam com 2 casas decimais. 
  
if dia_da_semana == "sábado" or dia_da_semana == "domingo": 
    print("Agradecemos a preferência, tenha um ótimo fim de semana!") 
elif dia_da_semana == "segunda-feira": 
    print("É um dia terrível, você não devia ter saído da cama.") 
elif dia_da_semana == "terça-feira": 
    print("Agradecemos a preferência, tenha uma ótima terça-feira!") 
elif dia_da_semana == "quarta-feira": 
    print("Agradecemos a preferência, tenha uma ótima quarta-feira!") 
elif dia_da_semana == "quinta-feira": 
    print("Agradecemos a preferência, tenha uma ótima quinta-feira!") 
elif dia_da_semana == "sexta-feira": 
    print("Agradecemos a preferência, tenha uma ótima sexta-feira!") 