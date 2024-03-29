menu = dict({
    "Pan": {
        "Producto" :list([
            {"nombre": "Pan de trigo", "valor": 800},
            {"nombre": "Pan de ajo", "valor": 1000},
            {"nombre": "Pan integral", "valor": 1500},
            {"nombre": "Bagette", "valor": 2000},
            {"nombre": "Pan tajado", "valor": 1000},
            {"nombre": "Rosca de maiz", "valor": 800},
            {"nombre": "Bollos suizos", "valor": 2000},
            {"nombre": "Bollitos de leche", "valor": 1500},
            {"nombre": "Pan de centeno", "valor": 3000},
            {"nombre": "Pan de bocadillo", "valor": 800},
        ]),
        "Promociones1": list([
            {"codigo" :8, "nombre": "compre 10", "valor": 25000},
            {"codigo" :5, "nombre": "compre 5", "valor": 8000},
            ])
    },
    "Pasteles": {
        "Productos" :list([
            {"nombre": "Pastel de chocolate", "valor": 2500},
            {"nombre": "Torta de fresa", "valor": 2500},
            {"nombre": "Hojaldre de manzana", "valor": 1500},
            {"nombre": "Rollos de canela", "valor": 2000},
            {"nombre": "Tiramisu", "valor": 2000},
            {"nombre": "Pastel de zanahoria", "valor": 2500},
            {"nombre": "Empanada de frutas'", "valor": 1500},
            {"nombre": "Donas glaseados'", "valor": 1000},
            {"nombre": "Croassants rellenos", "valor": 2500},
            {"nombre": "Milhojas", "valor": 1500},
        ]),
        "Promociones2": list([
            {"codigo" :6, "nombre": "compre 3", "valor": 3500},
            {"codigo" :9, "nombre": "compre 5", "valor": 6500},
        ])
    },
    "Galletas": {
        "Productoss" :list([
            {"nombre": "Galletas de avena", "valor": 1000},
            {"nombre": "Galletas de chocolate", "valor": 2000},
            {"nombre": "Alfajores", "valor": 2500},
            {"nombre": "Mantecados", "valor": 2000},
            {"nombre": "Palmeritas", "valor": 2000},
            {"nombre": "Barquillos", "valor": 1500},
            {"nombre": "Galletas con chispas", "valor": 1500},
            {"nombre": "Galettes", "valor": 2000},
            {"nombre": "Biscotti", "valor": 2500},
            {"nombre": "Galletas de jengibre", "valor": 1500},
        ]),
        "Promociones3": list([
            {"codigo":9, "nombre": "compre 5", "valor": 4000},
            {"codigo":0, "nombre": "compre 4", "valor": 5000},
        ])
    }
})

print("seleccione la categoria")
listaCategoria = list( menu.keys())
for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
opcioncategoria = int(input())
if opcioncategoria == 0:
    print(menu[listaCategoria[opcioncategoria]]["Producto"])
elif opcioncategoria == 1:
    print(menu[listaCategoria[opcioncategoria]]["Productos"])
elif opcioncategoria == 2:
    print(menu[listaCategoria[opcioncategoria]]["Productoss"])


print("seleccione el producto")
#listaCategorias1 = list(menu.items("Producto"))
for i, val in enumerate(menu["Producto"]):
    print(f"{i}. {val}")
opcioncategorias = int(input())

print(menu[opcioncategorias]["Productos"])


    
