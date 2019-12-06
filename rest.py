import unirest
import json

print "Introduzca 1 para listar, 2 para crear estudiante y 3 para consultar un estudiante"

opcion = raw_input()

if opcion == "1":
    estudiantes = unirest.get("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json" }).body
    for estudiante in estudiantes:
        if estudiante["correo"] != None:
            correo = estudiante["correo"]
        else:
            correo = " "
        if estudiante["matricula"] != None:
            matricula = estudiante["matricula"]
        else:
            matricula = " "
        if estudiante["carrera"] != None:
            carrera = estudiante["carrera"]
        else:
            carrera = " "

        print estudiante["nombre"] + " - " + str(matricula) + " - " + correo + " - " + carrera
        print ""


if opcion == "2":
    estudiante = {}
    print "Digite nombre: "
    estudiante['nombre'] = raw_input()
    print "Digite matricula: "
    estudiante['matricula'] = raw_input()
    print "Digite correo: "
    estudiante['correo'] = raw_input()
    print "Digite carrera: "
    estudiante['carrera'] = raw_input()

    unirest.post("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json" }, params=json.dumps(estudiante))

if opcion == "3":
    print "Digite matricula: "
    matricula = raw_input()
    estudiante = unirest.get("http://localhost:4567/rest/estudiantes/"+matricula, headers={ "Accept": "application/json" }).body

    if estudiante["correo"] != None:
        correo = estudiante["correo"]
    else:
        correo = " "
    if estudiante["matricula"] != None:
        matricula = estudiante["matricula"]
    else:
        matricula = " "
    if estudiante["carrera"] != None:
        carrera = estudiante["carrera"]
    else:
        carrera = " "

    print estudiante["nombre"] + " - " + str(matricula) + " - " + correo + " - " + carrera
