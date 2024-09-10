#funcao, calcular macros e montar dieta

#taxa metabolica basal homens
def TMB(peso, altura, idade):
    sexo = int(input("Digite 1 - masculino || 2 - feminino "))
    if(sexo == 1):
      tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.755 * idade)

      print("1 - sedentario")
      print("2 - levemente ativo")
      print("3 - moderadamente ativo")
      print("4 - Muito ativo")
      print("5 - extremamente ativo")
      nivel_atividade =  int(input("digite seu nivel de atividade fisica: "))

      if (nivel_atividade == 1):
        tmb = tmb * 1.2
      elif (nivel_atividade == 2):
        tmb = tmb * 1.375
      elif (nivel_atividade == 3):
        tmb = tmb * 1.55
      elif (nivel_atividade == 4):
        tmb = tmb * 1.725
      elif (nivel_atividade == 5):
        tmb = tmb * 1.9
      else:
        print("opcao invalida")
      
      #print(f"seu TMB é: {tmb:.2f}")
      return tmb

    elif(sexo == 2):
      tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * idade)

      print("1 - sedentario")
      print("2 - levemente ativo")
      print("3 - moderadamente ativo")
      print("4 - Muito ativo")
      print("5 - extremamente ativo")
      
      nivel_atividade =  int(input("digite seu nivel de atividade fisica: "))

      if (nivel_atividade == 1):
        tmb = tmb * 1.2
      elif (nivel_atividade == 2):
        tmb = tmb * 1.375
      elif (nivel_atividade == 3):
        tmb = tmb * 1.55
      elif (nivel_atividade == 4):
        tmb = tmb * 1.725
      elif (nivel_atividade == 5):
        tmb = tmb * 1.9
      else:
        print("opcao invalida")

      #print(f"seu TMB é: {tmb:.2f}")
      return tmb

    else:
      print('tente novamente')

#imc
def imc(peso, altura):
  altura_m = altura / 100
  imc = peso / (altura ** 2)

  if(imc < 18.5):
    print('Abaixo do peso')
    peso_magro = (imc + 18.5) / 2
  elif(imc >= 18.5 and imc < 24.9):
    print('Peso normal')
    peso_magro = (18.5 + 24.9) / 2
  elif(imc > 24.5 and imc < 29.9):
    print('Sobrepeso')
    peso_magro = (24.5 + 29.9) / 2
  elif(imc > 30):
    #print('obesidade')
    peso_magro = (30 + imc) / 2

  return peso_magro

#main
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em centimetros: "))
idade = int(input("Dig112ite sua idade: "))

#o quanto devo ingerir para emagrecer
Tp = TMB(peso, altura, idade) - 500


proteina_man = imc(peso, altura) * 2
proteina_fem = imc(peso, altura) * 1.6


#https://www.instagram.com/reel/CxYAoaXO4ZZ/?igsh=aWM2MHByM2d5MjFo
