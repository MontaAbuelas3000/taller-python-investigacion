
NUMERO_SECRETO = 42
MAX_INTENTOS = 5
intento = 1

print(" ADIVINA EL NÚMERO ")

while intento <= MAX_INTENTOS:
    numero = int(input(f"Intento {intento}/{MAX_INTENTOS} - Adivina el número: "))

    if numero == NUMERO_SECRETO:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif numero < NUMERO_SECRETO:
        print("El número secreto es MAYOR.")
    else:
        print("El número secreto es MENOR.")
    intento += 1

if intento > MAX_INTENTOS:
    print("Se acabaron los intentos. El número secreto era 42.")
