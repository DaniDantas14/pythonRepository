def transformMetrics (ValKM):
    ValM = int(ValKM * 1000)
    ValCM = int(ValKM * 100000)
    print(ValKM," Quilometros, corresponde à", ValM, " metros e à ",ValCM," centimetros!")

valor = float(input("Qual a medida em quilometros:"))
transformMetrics(valor)
