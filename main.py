# ejemplos de llamado de los otros scripts
import fuzzy_system
import FileDialog
version = "1.0.0"


class Platillo:
    def __init__(self, calorias, nombre, categorias, componentes, clase):
        self.calorias = calorias
        self.nombre = nombre
        self.categorias = categorias
        self.componentes = componentes
        self.clase = clase

    def __str__(self):
        mensaje = self.nombre + "\n"
        for componente in self.componentes:
            mensaje += componente + ', '
        mensaje += '.'
        return mensaje

def cargar_platillo():
    platillos = []
    platillos.append(Platillo('hipercalorico', 'burrito', ['mexicano', 'rapida'], ['pollo', 'cebolla', 'tortilla', 'salsa'], ['cena']))
    platillos.append(Platillo('hipercalorico', 'paella', ['mediterranea'], ['pollo', 'cerdo', 'arroz', 'calamar', 'mejillon', 'langostino'], ['almuerzo']))
    platillos.append(Platillo('calorico', 'olluquito con charqui', ['peruana', 'carne'], ['olluco', 'alpaca', 'papa'], ['algo']))
    platillos.append(Platillo('hipocalorico', 'rocoto relleno', ['peruana', 'carne'], ['aji', 'carne', 'huevo'], ['mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('calorico', 'antichucos', ['peruana', 'carne', 'asado'], ['corazon', 'res', 'aji', 'mazorca'], ['algo']))
    platillos.append(Platillo('hipocalorico', 'picante de cuy', ['peruana'], ['cuy', 'oregano', 'aji'], ['almuerzo','algo']))
    platillos.append(Platillo('calorico', 'huevos rancheros', ['mexicano'], ['frijol', 'huevo', 'tortilla', 'chile', 'pisto'], ['desayuno','cena']))
    platillos.append(Platillo('calorico', 'nachos', ['mexicano'], ['harina', 'cebolla', 'chile', 'queso'], ['merienda', 'algo']))
    platillos.append(Platillo('calorico', 'huarache', ['mexicano'], ['tortilla', 'queso', 'lechuga', 'pollo', 'frijol'], ['algo', 'cena']))
    platillos.append(Platillo('hipocalorico', 'ceviche de pescado', ['mexicano'], ['pescado', 'camaron', 'cebolla', 'limon', 'pimienta'], ['mediamanhana', 'merienda']))
    platillos.append(Platillo('hipercalorico', 'keshk', ['arabe', 'asado'], ['pollo', 'cebolla', 'yogurt', 'salsa'], ['almuerzo', 'algo']))
    platillos.append(Platillo('hipocalorico', 'croquetas falafel', ['arabe', 'vegetariana'], ['garbanzo', 'yogurt', 'salsa'], ['mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('calorico', 'baklava', ['arabe', 'postre'], ['nueces', 'miel', 'pasta', 'sesamo'], ['algo', 'merienda']))
    platillos.append(Platillo('calorico', 'shawarma', ['arabe', 'carne'], ['cordero', 'pollo', 'pan', 'vegetales', 'salsa'], ['cena', 'almuerzo']))
    platillos.append(Platillo('hipercalorico', 'lasagna de carne', ['carne', 'italiana', 'pasta'], ['harina', 'vegetales', 'berenjena', 'champinhon', 'atun'], ['almuerzo']))
    platillos.append(Platillo('calorico', 'pierna de cordero', ['carne', 'asado', 'mediterranea'], ['cordero', 'papa', 'verduras'], ['cena', 'almuerzo']))
    platillos.append(Platillo('calorico', 'arroz negro con calamar', ['mediterranea'], ['calamar', 'arroz', 'tomate', 'ajo', 'tinta'], ['almuerzo', 'cena']))
    platillos.append(Platillo('calorico', 'pizza mediterranea', ['italiana', 'rapida', 'mediterranea'], ['harina', 'tomate', 'pimiento', 'champinhon', 'atun'], ['cena', 'algo']))
    platillos.append(Platillo('calorico', 'chop suey', ['china', 'carne'], ['pollo', 'cerdo', 'apio', 'brotes', 'vegetales'], ['almuerzo','cena','algo']))
    platillos.append(Platillo('calorico', 'wantom mee', ['china'], ['fideo', 'huevo', 'cerdo', 'carne', 'cebolla'], ['desayuno', 'cena']))
    platillos.append(Platillo('hipocalorico', 'zongzi', ['china'], ['arroz', 'carne', 'judias', 'bamboo'], ['cena', 'algo', 'mediamanhana']))
    platillos.append(Platillo('calorico', 'pollo gong bao', ['china'], ['vegetales', 'cacahuate', 'pimienta'], ['almuerzo', 'cena']))
    platillos.append(Platillo('calorico', 'brownie con helado', ['postre'], ['harina', 'chocolate', 'nuez', 'huevo', 'helado'], ['algo', 'merienda']))
    platillos.append(Platillo('hipocalorico', 'postre de limon', ['postre', 'frio'], ['crema de leche', 'gelatina', 'limon', 'queso crema'], ['mediamanhana', 'algo', 'cena']))
    platillos.append(Platillo('hipocalorico', 'bizcocho de pinha', ['postre', 'caliente'], ['pinha', 'harina', 'huevo', 'mantequilla'], ['desayuno', 'mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('hipocalorico', 'mousse de coco', ['postre', 'frio'], ['coco', 'gelatina', 'miel', 'granada'], ['mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('hipocalorico', 'pannacotta con frambuesas', ['italiana', 'postre'], ['frambuesa', 'leche', 'crema de leche', 'vainilla'], ['mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('calorico', 'rajma', ['hindu', 'vegetariana'], ['frijol', 'especias', 'curry', 'pimienta'], ['desayuno', 'mediamanhana', 'almuerzo', 'algo', 'cena', 'merienda']))
    platillos.append(Platillo('calorico', 'pollo tandori', ['hindu', 'asado', 'carne'], ['pollo', 'especias', 'yogurt', 'pimienta'], ['desayuno', 'almuerzo', 'cena']))
    platillos.append(Platillo('hipercalorico', 'panipuri', ['hindu', 'vegetariana'], ['harina', 'tamarindo', 'chile', 'papa', 'garbanzo'], ['desayuno', 'mediamanhana', 'algo', 'merienda']))
    platillos.append(Platillo('calorico', 'biryani', ['hindu', 'carne'], ['carne', 'vegetales', 'yogurt', 'especias', 'arroz'], ['cena', 'algo', 'almuerzo']))
    platillos.append(Platillo('calorico', 'ravioli con albondigas', ['italiana', 'pasta', 'carne'], ['carne', 'huevo', 'queso', 'pasta', 'pimienta', 'salsa'], ['almuerzo', 'merienda']))
    platillos.append(Platillo('calorico', 'spagetti carbonara', ['italiana', 'pasta', 'carne'], ['carne', 'tomate', 'queso', 'pasta', 'pimienta'], ['cena', 'almuerzo']))
    platillos.append(Platillo('hipercalorico', 'hamburguesa', ['rapida', 'carne'], ['carne', 'pan', 'queso', 'lechuga'], ['almuerzo', 'algo']))
    platillos.append(Platillo('calorico', 'tamal', ['tipica', 'carne'], ['harina', 'papa', 'zanahoria', 'carne'], ['desayuno', 'cena', 'almuerzo']))
    platillos.append(Platillo('hipercalorico', 'mondongo', ['tipica', 'carne'], ['carne', 'papa', 'mazorca', 'yuca', 'zanahoria'], ['almuerzo']))
    platillos.append(Platillo('hipercalorico', 'bandeja paisa', ['tipica', 'carne'], ['frijol', 'arroz', 'chicarron', 'huevo', 'carne'], ['almuerzo']))
    platillos.append(Platillo('hipocalorico', 'tequila', ['mexicano'], ['limon', 'tequila', 'sal'], ['merienda']))
    platillos.append(Platillo('hipercalorico', 'filete al horno', ['carne'], ['carne', 'champinhones', 'tomate'], ['almuerzo']))
    platillos.append(Platillo('calorico', 'lasagna vegetariana', ['italiana', 'vegetariana', 'pasta'], ['pasta', 'champinhones', 'zanahoria', 'berenjena', 'salsa'], ['cena', 'algo', 'almuerzo']))
    platillos.append(Platillo('hipercalorico', 'ramen', ['china', 'vegetariana', 'pasta'], ['pasta', 'champinhones', 'zanahoria', 'berenjena', 'salsa'], ['desayuno', 'algo', 'almuerzo', 'mediamanhana', 'cena', 'merienda']))


    return platillos

def seleccionar(platillos, clase, calorico):
    aux = [platillo for platillo in platillos if clase in platillo.clase and calorico in platillo.calorias]
    antes = []
    while len(aux) > 1:
        if aux[0].categorias != []:
            categoria = aux[0].categorias[0]
            eleccion = raw_input("Quiere que su comida sea " + categoria + '?\n(formato: "si" o "no") ')
            if eleccion.lower() == 'no':
                aux = [platillo for platillo in aux if categoria not in platillo.categorias]
            else:
                for platillo in aux:
                    if categoria in platillo.categorias:
                        platillo.categorias.pop()
                        aux.append(platillo)        
        else:
            for componente in aux[0].componentes:
                if len(aux) > 1:
                    if componente not in antes:
                        eleccion = raw_input("Quiere que su comida contenga " + componente + '?\n(formato: "si" o "no") ')
                        if eleccion.lower() == 'no':
                            aux = sorted(set([platillo for platillo in aux if componente not in platillo.componentes]))
                        elif eleccion.lower() == 'si':
                            aux = sorted(set([platillo for platillo in aux if componente in platillo.componentes]))
                            antes.append(componente)
                        else:
                            print 'Formato no valido'
                            continue
    else:
        if aux != []:
            return aux[0]
        else:
            print "Lo sentimos, por ahora no tenemos un platillo para recomendar \nque se ajuste a sus gustos"

def pregunta_hora():
	horario = raw_input("A que horas piensa comer? (formato: Horas:minutos) \n Ejemplo: 14:35 o 02:15 \n ")
	try:
		minutos = int(horario[0:2]) * 60
		minutos += int(horario[3:])
		clase, tipo = fuzzy_system.rule_hora(minutos)
		return clase, tipo
	except:
		print "Formato no valido"
		return None, "Error"

def pregunta_actividad():
	actividad = raw_input("Realizara o realizo ejercicio antes o despues de la comida? (formato: 'si' o 'no')\n")
	if actividad.lower() not in ["si", "no"]:
		print ("Actividad no valida")
	elif actividad.lower() == "si":
		intensidad = raw_input("Que tan intensa sera la actividad? \n ingrese un numero de 5 a 10, donde 5 es actividad dia a dia y 10 entrenamientos extensivos\n(formato: numero entero)\n Ejemplo: 7\n")
	elif actividad.lower() == "no":
		intensidad = raw_input("Ya que no realizara ejercicio \n Que tan activo sera su dia?\n Ingrese un numero entero de 0 a 5, donde 0 es reposo y 5 son actividades cotidianas\n Ejemplo: 3 \n")
	try:
		intensidad = int(intensidad)
		calorico, tipo = fuzzy_system.rule_actividad(intensidad)
		return calorico, tipo
	except:
		print "Formato no valido"
		return None, "Error"

def clasificar(clase):
    result = {'1': 'desayuno',
    '2': 'desayuno',
    '3': 'mediamanhana',
    '4': 'almuerzo',
    '5': 'almuerzo',
    '6': "algo",
    '7': 'algo',
    '8': 'cena',
    '9': 'cena',
    '10': 'merienda',
        }
    result = result[clase]
    return result

def calorias(calorico):
    if calorico <= 350:
        result = 'hipocalorico'
    elif calorico > 420 and calorico <= 600:
        result = 'calorico'
    elif calorico > 600:
        result = 'hipercalorico'
    return result


def main():
    print "Bienvenido a EasyMeal sistema de recomendacion de comidas. Version: " + version
    while(True):
        elegido = False
        platillos = cargar_platillo()
    	clase, tipo = pregunta_hora()
    	while(clase == None):
    		clase, tipo = pregunta_hora()
        clase = clasificar(str(int(clase)))
    	calorico, tipo = pregunta_actividad()
    	while(calorico == None):
    		calorico, tipo = pregunta_actividad()
        calorico = calorias(calorico)
        platillo = seleccionar(platillos, clase, calorico)
        if platillo != None:
            print "Te recomendamos: " + platillo.__str__() + '\n\n'


if __name__ == "__main__": main()