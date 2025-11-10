
print(" LISTA DE COMPRAS ")
total = 0
productos = int(input("¿Cuántos productos vas a comprar? "))

for i in range(1, productos + 1):
    nombre = input(f"Nombre del producto {i}: ")
    precio = float(input(f"Precio de {nombre}: $"))
    total += precio

print(f"\nTotal sin descuento: ${total:.2f}")

if total > 100:
    descuento = total * 0.10
    total -= descuento
    print(f"Se aplicó un descuento de 10% (${descuento:.2f})")

print(f"Total final a pagar: ${total:.2f}")
