scoreJuan = 0
scorePedro = 0
scoreMario = 0
scoreLuis = 0

print("**JUEGO DE CARTAS**")
print("Round 01")
Juan01 = int(input("¿Cuál es la carta de Juan? "))
if (Juan01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Pedro01 = int(input("¿Cuál es la carta de Pedro? "))
if (Pedro01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Mario01 = int(input("¿Cuál es la carta de Mario? "))
if (Mario01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Luis01 = int(input("¿Cuál es la carta de Luis? "))
if (Luis01 > 10):
  print ("Solo se permiten valores del 1 al 10")

if (Juan01 > Pedro01 and Juan01 > Mario01 and Juan01 > Luis01):
  print("Ganó Juan")
  scoreJuan = scoreJuan + 1
if (Pedro01 > Juan01 and Pedro01 > Mario01 and Pedro01 > Luis01):
  print ("Gano Pedro")
  scorePedro = scorePedro + 1
if (Mario01 > Juan01 and Mario01 > Pedro01 and Mario01 > Luis01):
 print ("Gano Mario")
 scoreMario = scoreMario + 1
if (Luis01 > Juan01 and Luis01 > Pedro01 and Luis01 > Mario01):
 print ("Gano Luis")
 scoreLuis = scoreLuis + 1
print ("Puntuación del Round 01:")
print ("Juan: " + str(scoreJuan))
print ("Pedro: " + str(scorePedro))
print ("Mario: " + str(scoreMario))
print ("Luis: " + str(scoreLuis))

print("---------------------------")
print("Round 02")
Juan01 = int(input("¿Cuál es la carta de Juan? "))
if (Juan01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Pedro01 = int(input("¿Cuál es la carta de Pedro? "))
if (Pedro01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Mario01 = int(input("¿Cuál es la carta de Mario? "))
if (Mario01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Luis01 = int(input("¿Cuál es la carta de Luis? "))
if (Luis01 > 10):
  print ("Solo se permiten valores del 1 al 10")

if (Juan01 > Pedro01 and Juan01 > Mario01 and Juan01 > Luis01):
  print("Ganó Juan")
  scoreJuan = scoreJuan + 1
if (Pedro01 > Juan01 and Pedro01 > Mario01 and Pedro01 > Luis01):
  print ("Gano Pedro")
  scorePedro = scorePedro + 1
if (Mario01 > Juan01 and Mario01 > Pedro01 and Mario01 > Luis01):
 print ("Gano Mario")
 scoreMario = scoreMario + 1
if (Luis01 > Juan01 and Luis01 > Pedro01 and Luis01 > Mario01):
 print ("Gano Luis")
 scoreLuis = scoreLuis + 1
print ("Puntuación del Round 02:")
print ("Juan: " + str(scoreJuan))
print ("Pedro: " + str(scorePedro))
print ("Mario: " + str(scoreMario))
print ("Luis: " + str(scoreLuis))

print("---------------------------")
print("Round 03")
Juan01 = int(input("¿Cuál es la carta de Juan? "))
if (Juan01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Pedro01 = int(input("¿Cuál es la carta de Pedro? "))
if (Pedro01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Mario01 = int(input("¿Cuál es la carta de Mario? "))
if (Mario01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Luis01 = int(input("¿Cuál es la carta de Luis? "))
if (Luis01 > 10):
  print ("Solo se permiten valores del 1 al 10")

if (Juan01 > Pedro01 and Juan01 > Mario01 and Juan01 > Luis01):
  print("Ganó Juan")
  scoreJuan = scoreJuan + 1
if (Pedro01 > Juan01 and Pedro01 > Mario01 and Pedro01 > Luis01):
  print ("Gano Pedro")
  scorePedro = scorePedro + 1
if (Mario01 > Juan01 and Mario01 > Pedro01 and Mario01 > Luis01):
 print ("Gano Mario")
 scoreMario = scoreMario + 1
if (Luis01 > Juan01 and Luis01 > Pedro01 and Luis01 > Mario01):
 print ("Gano Luis")
 scoreLuis = scoreLuis + 1
print ("Puntuación del Round 03:")
print ("Juan: " + str(scoreJuan))
print ("Pedro: " + str(scorePedro))
print ("Mario: " + str(scoreMario))
print ("Luis: " + str(scoreLuis))

print("---------------------------")
print("Round 04")
Juan01 = int(input("¿Cuál es la carta de Juan? "))
if (Juan01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Pedro01 = int(input("¿Cuál es la carta de Pedro? "))
if (Pedro01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Mario01 = int(input("¿Cuál es la carta de Mario? "))
if (Mario01 > 10):
  print ("Solo se permiten valores del 1 al 10")
Luis01 = int(input("¿Cuál es la carta de Luis? "))
if (Luis01 > 10):
  print ("Solo se permiten valores del 1 al 10")

if (Juan01 > Pedro01 and Juan01 > Mario01 and Juan01 > Luis01):
  print("Ganó Juan")
  scoreJuan = scoreJuan + 1
if (Pedro01 > Juan01 and Pedro01 > Mario01 and Pedro01 > Luis01):
  print ("Gano Pedro")
  scorePedro = scorePedro + 1
if (Mario01 > Juan01 and Mario01 > Pedro01 and Mario01 > Luis01):
 print ("Gano Mario")
 scoreMario = scoreMario + 1
if (Luis01 > Juan01 and Luis01 > Pedro01 and Luis01 > Mario01):
 print ("Gano Luis")
 scoreLuis = scoreLuis + 1
print ("Puntuación del Round 04:")
print ("Juan: " + str(scoreJuan))
print ("Pedro: " + str(scorePedro))
print ("Mario: " + str(scoreMario))
print ("Luis: " + str(scoreLuis))

if (scoreJuan > scorePedro and scoreJuan > scoreMario and scoreJuan > scoreLuis):
  print("El ganador final es Juan")
if (scorePedro > scoreJuan and scorePedro > scoreMario and scorePedro > scoreLuis):
  print("El ganador final es Pedro")
if (scoreMario > scoreJuan and scoreMario > scorePedro and scoreMario > scoreLuis):
  print("El ganador final es Mario")
if (scoreLuis > scoreJuan and scoreLuis > scorePedro and scoreLuis > scoreMario):
  print("El ganador final es Luis")