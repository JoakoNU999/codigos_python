print("Almacen YUYITO")
valor_bebida=int(input("Ingrese valor bebida"))
p_az=float(input("Ingrese porcentaje de azucar(0-100)"))
impuesto=0
if paz_>= 0 and p_az<=15:
    impuesto=0.20
    
if p_az>=16 and p_az<= 25:
    impuesto=0.30
valor_impu=valor_bebida*impuesto
print(f"el valor del impuesto es {valor_impu}")
valor_jabaa_impu=valor_impu*8
print(f"El valor del impuesto por jabaa es de {valor_jabaa_impu}")