sample_dict = {
    "class": {
        "student": {
            "Nombre": "Mike",
            "notas": {
                "Fisica": 70,
                "Historia": 80,
		            "Matematica": 90
            },
        }
    }
}
def calcular_notas(dict):
    nombre = dict["class"]["student"]["Nombre"]
    nota_fisica = dict["class"]["student"]["notas"]["Fisica"]
    nota_historia = dict["class"]["student"]["notas"]["Historia"]
    nota_mate = dict["class"]["student"]["notas"]["Matematica"]
    promedio = (nota_fisica + nota_historia + nota_mate)/3
    return {"Nombre": nombre, "Nota promedio": promedio}
print(calcular_notas(sample_dict))