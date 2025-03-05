 #Paso 1: Solicitar datos al usuario
nombre = input("Ingrese su nombre completo: ")  # Ahora se deja al usuario escribir el nombre
edad = int(input("Ingrese su edad: "))  # El usuario ingresa su edad sin valores predeterminados
dias_vividos = int(input("Ingrese la cantidad de días vividos en Medellín: "))  # Igualmente sin valor predeterminado
estrato = int(input("Ingrese su estrato (0 - 6): "))  # Solicitar estrato sin valor predeterminado
ocupacion = input("Ingrese su ocupación (empleado del gobierno, desempleado, empleado del sector privado, otro): ").strip().lower()

# Paso 2: Calcular impuestos según el estrato
impuesto_base = 0  # Valor inicial del impuesto

# Verificamos el estrato e inicializamos el impuesto en consecuencia
if estrato == 0:
    impuesto_base = 0
elif estrato in [1, 2]:
    impuesto_base = 500 * dias_vividos
elif estrato in [3, 4]:
    impuesto_base = (50000 * dias_vividos) + 1000000
elif estrato in [5, 6]:
    impuesto_base = 250000 * dias_vividos
else:
    print("Estrato no válido.")
    exit()  # Termina el programa si el estrato ingresado es inválido

# Paso 3: Aplicar descuentos según la ocupación
descuento = 0  # Inicializamos el descuento en 0

# Aseguramos que el usuario ingrese una ocupación válida
if ocupacion == "empleado del gobierno":
    descuento = 0.50  # 50% de descuento
elif ocupacion == "desempleado":
    descuento = 0.10  # 10% de descuento
elif ocupacion == "empleado del sector privado":
    descuento = 0.05  # 5% de descuento
else:
    print("Ocupación no válida. Se aplicará un descuento del 0%.")
    descuento = 0  # Si la ocupación no es válida, no se aplica descuento

# Paso 4: Calcular impuesto final después del descuento
descuento_impuesto = impuesto_base * descuento
impuesto_final = impuesto_base - descuento_impuesto

# Paso 5: Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Días vividos en Medellín: {dias_vividos}")
print(f"Estrato: {estrato}")
print(f"Ocupación: {ocupacion.capitalize()}")
print(f"Impuesto sin descuento: ${impuesto_base:,}")
print(f"Descuento aplicado ({descuento * 100}%): ${descuento_impuesto:,}")
print(f"Total a pagar después del descuento: ${impuesto_final:,}")
