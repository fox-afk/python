# calculo de media

notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 7:
  notas[x]: float(input(f"Nota:{x}: "))
  soma += notas[x]
  x+=1
x = 0
while x < 7:
 print(f"{x}: {notas[x]:6.2f}")
x += 1
print(f"media:{soma / x:5.2f}")