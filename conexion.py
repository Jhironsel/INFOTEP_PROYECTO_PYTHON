import firebirdsql
#La linea de arriba es la utilizada para hacer el import de firebirdsql
#Para realizar este import primero debes instalar la siguiente libreria
#de python pip install firebirdsql

# Creando el objecto conn, el cual tendrá la conexión a la base datos.
conn = firebirdsql.connect(
    host='localhost',
    database='/home/jhironsel/Documentos/Curso de Big Data/Mod. 2 - Manejo y Diseño de Base de Datos - Part. 2/INFOTEP_BIGDATA.FDB',
    port=3050,
    user='sysdba',
    password='Seguridad4321'
)

# Verificamos la conexión a la base de datos. 
if conn:
    print("Conexion exitosa.")

# Eliminamos todos los registro de la base de datos para cuestiones practica. 
cur = conn.cursor()
cur.execute("DELETE FROM PARTICIPANTE;")
conn.commit()

# Los datos a continuacion son los que seran insertado a la base de datos. 

nuevosDatos = [
('699-6477188-6', 'Sebastian', 'Lang', '1998, 1, 15', '(583) 724-7141', '1-198-656-4878',
'302-1604 Et Ave', 'S', 'aliquam.nisl.nulla@hotmail.net', 'F', 'Peluqueria',
'76.00', '95.00', '85.00', '73.00'),

('725-3166196-3', 'Garrison', 'Mercer', '1999, 3, 27', '(424) 888-6407', '1-489-536-2616',
'484-8989 Enim. Street', 'S', 'non@google.org', 'M', 'JAVA',
'83.00', '74.00', '70.00', '90.00'),

('752-0136678-9', 'Burton', 'Hodge', '2000, 10, 9', '(334) 641-5434', '1-680-194-7675',
'P.O. Box 172, 2516 Dis Av.', 'U', 'mollis@google.edu', 'F', 'JAVA', 
'77.00', '70.00', '74.00', '95.00'),

('782-2374777-1', 'Philip', 'Griffith', '1993, 8, 24', '(366) 186-8345', '1-655-668-1277',
'9839 Nunc Avenue', 'U', 'eleifend.cras@aol.org', 'M', 'JAVA',
'90.00', '74.00', '94.00', '84.00'),

('281-4783641-0', 'Gray', 'Frost', '1985, 4, 18', '(294) 289-2555', '1-389-575-8647',
'739-3583 Diam St.', 'V', 'massa.vestibulum@hotmail.ca', 'F', 'Peluqueria',
'74.00', '91.00', '70.00', '95.00'),

('187-6812415-6', 'Lavinia', 'Bolton', '1988, 12, 10', '(977) 326-4147', '1-283-381-4225', 
'Ap #288-3700 Penatibus Rd.', 'V', 'sollicitudin.commodo@protonmail.com', 'M', 'JAVA', 
'79.00', '66.00', '94.00', '78.50'),

('707-3824941-3', 'Reuben', 'Gibbs', '1994, 4, 22', '(737) 649-2327', '1-762-428-4428', 
'P.O. Box 392, 4052 Imperdiet St.', 'C', 'vivamus@aol.com', 'F', 'Ofimatica', 
'94.00', '91.00', '80.00', '72.00'),

('130-4872883-2', 'Harriet', 'Robertson', '1984, 12, 23', '(805) 487-1875', '1-421-327-8756',
'Ap #299-7018 Maecenas Av.', 'C', 'fringilla.mi@protonmail.couk', 'M', 'JAVA',
'86.00', '69.00', '94.00', '96.00'),

('947-9828364-8', 'Adara', 'Morse', '1983, 7, 31', '(516) 257-6165', '1-117-756-5141',
'P.O. Box 837, 3664 Diam Rd.', 'S', 'nulla.interdum.curabitur@protonmail.org', 'F', 'Peluqueria',
'96.00', '65.00', '61.00', '92.00'),

('123-1782851-5', 'Ana', 'Flawer', '1991, 2, 25', '(373) 466-8616', '1-495-753-4877',
'4318 Nonummy. St.', 'S', 'luctus.ipsum@protonmail.ca', 'M', 'JAVA', 
'83.00', '75.00', '79.00', '72.00'),

('798-7338272-5', 'Brett', 'Morris', '1983, 5, 9', '(475) 582-1481', '1-255-429-3356',
'P.O. Box 867, 8559 Erat Street', 'U', 'sapien@protonmail.net', 'F', 'JAVA', 
'63.00', '80.00', '73.00', '72.00'),

('485-7231542-7', 'Barry', 'Larsen', '1993, 10, 28', '(215) 682-2914', '1-842-347-4734',
'Ap #116-6185 In St.', 'U', 'aliquam.adipiscing@aol.edu', 'M', 'JAVA',
'79.00', '68.00', '75.00', '88.00'),

('532-1846514-3', 'Regina', 'Clay', '1989, 10, 4', '(906) 395-7192', '1-483-720-3412',
'Ap #453-6429 Sit Street', 'V', 'ornare.sagittis@outlook.net', 'F', 'JAVA',
'95.00', '57.00', '83.00', '93.00'),

('481-7467428-5', 'Ivy', 'Fowler', '1981, 10, 27', '(728) 675-1913', '1-111-272-9478',
'Ap #973-6285 Praesent Ave', 'V', 'in.consectetuer@yahoo.org', 'M', 'Peluqueria',
'70.00', '75.00', '79.00', '77.00'),

('498-1860775-2', 'Camilla', 'Barnes', '1984, 2, 22', '(641) 100-6927', '1-522-434-9847',
'1707 Id, Ave', 'C', 'in.lorem@google.net', 'F', 'Ofimatica', '68.00', '51.00', '93.00', '99.00')
]

print('Cantidad de registros: ', len(nuevosDatos))

# Creamos o instaciamos un nuevo objecto cursor para la insersion masiva de los datos.
cur = conn.cursor()

# El objecto cur contiene un metodo que nos permite pasarle un query y un arreglo con los datos que necesitamos 
# insertar a la base de datos. Dicho metodo es el executemany(query, arreglo));

cur.executemany('''
    INSERT INTO PARTICIPANTE (CEDULA, NOMBRES, APELLIDOS, FECHA_NACIMIENTO, TELEFONO, CELULAR, DIRECCION, ESTADO_CIVIL,
         CORREO_ELECTRONICO, SEXO, CURSO, MODULO_1, MODULO_2, MODULO_3, MODULO_4)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
''', nuevosDatos)

# Guardamos los datos con el metodo commit();
conn.commit()


# Eliminamos tres registros de la base de datos.
cur = conn.cursor()
cur.execute('''
    DELETE 
    FROM PARTICIPANTE 
    WHERE CEDULA IN('798-7338272-5','707-3824941-3','752-0136678-9');
''')
conn.commit()

# Actualizamos 5 registros de la base de datos.
#1
cur = conn.cursor()
cur.execute('''
    UPDATE PARTICIPANTE a
    SET 
        a.TELEFONO = '(215) 682-5555'
    WHERE
        a.CEDULA = '485-7231542-7';
''')
conn.commit()

#2
cur = conn.cursor()
cur.execute('''
    UPDATE PARTICIPANTE a
    SET 
        a.CELULAR = '1-495-753-4877'
    WHERE
        a.CEDULA = '123-1782851-5';
''')
conn.commit()

#3
cur = conn.cursor()
cur.execute('''
    UPDATE PARTICIPANTE a
    SET 
        a.DIRECCION = 'Calle 27 de febrero, San Juan.'
    WHERE
        a.CEDULA = '498-1860775-2';
''')
conn.commit()

#4
cur = conn.cursor()
cur.execute('''
    UPDATE PARTICIPANTE a
    SET 
        a.CORREO_ELECTRONICO = 'cambiado@listo.com.do'
    WHERE
        a.CEDULA = '699-6477188-6';
''')
conn.commit()

#5
cur = conn.cursor()
cur.execute('''
    UPDATE PARTICIPANTE a
    SET 
        a.TELEFONO = '(215) 682-2020', 
        a.CELULAR = '1-495-555-4877', 
        a.DIRECCION = 'Calle Colon #23, Guachupita', 
        a.CORREO_ELECTRONICO = 'guachupitero@gmail.com'
    WHERE
        a.CEDULA = '130-4872883-2';
''')
conn.commit()

# Mostrar resultados en la base de datos.
cur = conn.cursor()
cur.execute("SELECT PARTICIPANTE_ID, CEDULA, NOMBRES, APELLIDOS, FECHA_NACIMIENTO, "+
                    "TELEFONO, CELULAR, DIRECCION, ESTADO_CIVIL, CORREO_ELECTRONICO, "+
                    "SEXO, CURSO, MODULO_1, MODULO_2, MODULO_3, MODULO_4, PROMEDIO "+
            "FROM PARTICIPANTE;")
for c in cur.fetchall():
    print(c)

print('Cantidad de filas o registros en el cursor actual: '+str(cur.rowcount))

conn.close()
