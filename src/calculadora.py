

print("=== CALCULADORA SIMPLE ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

while True:
    print("\nElige una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Opción (1-5): ")
    if opcion == "5":
        print("¡Adiós!")
        break
    if opcion == "1":
      resultado = num1 + num2
      print(f"La suma es: {resultado}")
    elif opcion == "2":
      resultado = num1 - num2
      print(f"La resta es: {resultado}")
    elif opcion == "3":
      resultado = num1 * num2
      print(f"La multiplicación es: {resultado}")
    elif opcion == "4":
      if num2 != 0:
          resultado = num1 / num2
          print(f"La división es: {resultado}")
    else:
        print("Error: no se puede dividir entre cero")

