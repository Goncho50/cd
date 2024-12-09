"""
Arquitectura basada en (micro)servicios REST - Servidor
"""
#NOTA CAMBIAR EL PUERTO POR SI ESTÁ OCUPADO EN EL DISPOSITIVO Y DA ERROR

from flask import Flask, request, jsonify
import sqlite3,pandas as pd
from flask_cors import CORS

app = Flask(__name__)
# Configuramos CORS para permitir que lleguen solicitudes desde http://localhost:8080
CORS(app, origins=["http://localhost:8080"])


proyectos=[
           ( 'Haskell',  'En el primer año cursamos la asignatura programación funcional y lógica, donde aprendimos a manejar diversos lenguajes. \nUno de los proyectos de prácticas de dicha asignatura eran una serie de numerosos ejercicios de Haskell para comprender cómo era la programación funcional. \nEstos eran bastante tediosos y no era fácil encontrar una solución rápida. Haskell cuenta con una sintaxis difícil, lo que supuso un verdadero reto para nosotros ya que solo llevábamos unos meses programando con Python. \nPor otro lado, se daban una gran cantidad de errores de compilación, en su mayoría debidos a que Haskell tiene un tipado estático y muy rígido, algo a lo que no estábamos acostumbrados. \nEsta práctica se alargó dos meses y muchos compañeros consideran que ha sido la práctica más difícil que hemos tenido.' ,"src/assets/haskell.png"),
            ('Java', 'Se dio en el segundo año en Programación Concurrente y Distribuida. \nEstas prácticas fueron claves para alcanzar un conocimiento sólido de Java, ya que no lo habíamos tocado antes. También fue vital para entender cómo funciona la estructura de cliente-servidor. \nMediante sockets, dejábamos al servidor a la espera de clientes que se podían conectar a él y pedirle que hiciera ciertos procesos, como guardar palabras con distintos significados, y el servidor escribiría en una base de datos. \nEsta práctica fue bastante larga y difícil pero la mayoría aprendimos mucho de ella.' ,'src/assets/java.png'),
            ('BBDD',  'Nuestra primera experiencia manejando bases de datos fue el curso pasado en Modelado, Almacenamiento y Gestión de Datos. En las prácticas se nos daba un CSV con una gran candidad de películas, con sus correspondientes actores, fechas de salida, reseñas etc. \nLo importante era tratar toda esa información para poder meterla en una base de datos de PostgreSQL y hacer ahí querys con SQL. Después tuvimos que hacer lo mismo con MongoDB, y así también practicábamos con bases de datos no relacionales. \nEstas prácticas en general no fueron de nuestro agrado porque hacía falta comprender muy bien cómo funcionaba PostgreSQL y muchos comandos en Linux, y nos atascábamos bastante.' ,''),
            ('Computación',  'En el segundo año cursamos la asignatura de arquitecturas de computación, donde aprendimos el funcionamiento de el lenguaje ensamblador y empleamos RARS para observar el proceso de traducción de las órdenes desde el lenguaje de programación hasta el lenguaje ensamblador.' ,'src/assets/rars.png'),
            ('Prolog', 'En el primer año cursamos la asignatura programación funcional y lógica, donde aprendimos a manejar diversos lenguajes. \nUno de los proyectos de prácticas de dicha asignatura eran una serie de numerosos ejercicios de Prolog para comprender cómo era la programación lógica. \nA pesar de ser nuestro primer contacto con este tipo de programación, nuestros resultados fueron excelentes. \nResolvimos con éxito varios problemas lógicos que involucraban conocimientos teóricos como algoritmos de resolución de grafos (como Dijkstra) y aprendimos sobre el funcionamiento de Prolog en profundidad.' ,'')
        ]


@app.route('/regenerar_bd', methods=['POST'])
def regenerar_bd():

    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()


    cursor.execute("DROP TABLE IF EXISTS proyectos")
    cursor.execute("""CREATE TABLE proyectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        desc TEXT NOT NULL,
        link_foto TEXT)""")

    for proyecto in proyectos:
        cursor.execute(f"""INSERT INTO proyectos (nombre,desc,link_foto) values (?,?,?)""",proyecto)

    conexion.commit()
    conexion.close()
    return jsonify({"resultado": 'se han cargado los proyectos por defecto en la base de datos'})


@app.route('/coger_proyectos', methods=['GET'])
def coger_proyectos():
    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()


    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall() ; print(proyectos)

    conexion.commit()
    conexion.close()
    dicts=[]
    for elem in proyectos:
        d={'id':elem[0],'name':elem[1],'desc': elem[2] ,'fotopath':elem[3]}
        dicts.append(d)
    return jsonify(dicts) #devulevo una lista de dicts, cada dict es un proyecto

@app.route('/eliminar_proyecto', methods=['DELETE'])
def eliminar_proyecto(): #HABRIA QUE PEDIR AUTENTICACIÓN!!!

    data=request.json ; print(data);nombre = data['nombre']
    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()


    cursor.execute("DELETE FROM proyectos WHERE nombre = ?", (nombre,))
    #proyectos = cursor.fetchall() ; print(proyectos)
    conexion.commit()

    conexion.close()

    return jsonify({"resultado": f'se ha eliminado el proyecto de {nombre}'})

@app.route('/añadir_proyecto', methods=['PUT'])
def añadir_proyecto(): #HABRIA QUE PEDIR AUTENTICACIÓN!!!

    data=request.json ; print(data);
    proyecto =data['tupla']
    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()

    cursor.execute(f"""INSERT INTO proyectos (nombre,desc,link_foto) values (?,?,?)""",proyecto)
    #proyectos = cursor.fetchall() ; print(proyectos)
    conexion.commit()

    conexion.close()

    return jsonify({"resultado": 'se ha añadido el proyecto'})

@app.route('/editar_proyecto', methods=['PUT'])
def editar_proyecto(): #HABRIA QUE PEDIR AUTENTICACIÓN!!!

    data=request.json ; modificaciones=data['modificaciones'] ; nombre=data['proyecto a editar'] ; campos_a_editar=data['campos a editar']

    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()


    query='UPDATE proyectos SET' ;
    print(campos_a_editar)
    for key in campos_a_editar:
        print(key,campos_a_editar[key])
        if campos_a_editar[key]==True:
            query += f' {key}=?,'
    query=query[:-1] + ' WHERE nombre=?' #nos quitamos la ultima coma con el :-1
    modificaciones_sin_none = tuple(x for x in modificaciones if x.strip())+(nombre,)
    print(query)

    cursor.execute(query,modificaciones_sin_none)
    #proyectos = cursor.fetchall() ; print(proyectos)
    conexion.commit()

    conexion.close()

    return jsonify({"resultado": 'se ha modificado el proyecto'})




if __name__ == "__main__":
    app.run(port=7050)