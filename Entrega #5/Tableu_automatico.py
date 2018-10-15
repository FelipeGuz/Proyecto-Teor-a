#-*-coding: utf-8-*-
negacion = '~'
Y = '&'
O = 'v'
implicacion = '>'

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

#creo letras proposicionales
letrasproposicionales = []
for i in range(1, 31):
	letrasproposicionales.append(str(i))

#Regla 1, no pueden haber 3 objetos en la misma casilla
formula = ""
times = 0
for i in letrasproposicionales:
	implica = ""
	p = int(i)
	if p in range(1, 11):
		implica = str(p+10)+','+negacion+str(p+20)+','+negacion+Y+i+','+implicacion
	if p in range(11, 21):
		implica = str(p-10)+','+negacion+str(p+10)+','+negacion+Y+i+','+implicacion
	if p in range(21, 31):
		implica = str(p-20)+','+negacion+str(p-10)+','+negacion+Y+i+','+implicacion
	if times == 0:
		formula = implica
	else:
		formula += implica+Y
	times += 1
#Regla 2: Solo hay 2 bombas
letrasauxiliar = []
for i in range(1, 11):
	letrasauxiliar.append(str(i))
other = 0
for i in letrasauxiliar:
	aux = [x for x in letrasauxiliar if x != i]
	for j in aux:
		aux2 = [x for x in aux if x != j]
		implica = ""
		times = 0
		for p in aux2:
			if times == 0:
				implica = p+','+negacion
			else:
				implica = implica+p+','+negacion+Y
			times += 1
		implica = implica+j+','+i+','+Y+implicacion
	formula += implica+Y
#Regla 3: regla para los unos
formula += "11,2,>"+Y
for i in range(2, 10):
		conjuncion1 = str(i-1)+','+str(i+1)+','+negacion+Y
		conjuncion2 = str(i-1)+','+negacion+str(i+1)+','+Y
		disyuncion = conjuncion1+conjuncion2+O;
		implica = str(10+i)+','+disyuncion+implicacion
		formula += implica+Y
formula += "20,10,>"+Y
#Regla 4: regla para los 2:
formula += "21,"+negacion+Y
for i in range(2, 10):
	conjuncion = str(i-1)+','+str(i+1)+','+Y
	implica = str(20+i)+','+conjuncion+implicacion
	formula += implica+Y
formula += "30,"+negacion+Y
A = T.StringtoTree(formula, letrasproposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]]

OK = ''
interpretaciones = []

OK, INTS = T.Tableaux(lista_hojas, letrasproposicionales)
print "Tableau terminado!"

end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo
        import visualizacion as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"