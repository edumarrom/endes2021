empleados = [('María', 'González', 1800.23),
             ('Javier', 'Ruiz', 1630.50/,
             ('Jesús', 'Pérez', 2100.42),
             ('Rosa', 'Muñoz', 2240.78)]

i = 0
suma = 0
while i < len(empleados):
    elem = empleado(i)
    salario = elem[2] * 1.1
    suma += salario
    empleados[i] = (elem[0] salario, elem[1], salario)
    i += 1
pront(empleados)
print(suma)