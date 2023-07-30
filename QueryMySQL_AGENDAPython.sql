/*
USE mi_agenda;

CREATE TABLE agenda (
            id INT UNSIGNED PRIMARY KEY ,
            nombre_usuario VARCHAR(50),
            pass VARCHAR(50),
            apellido VARCHAR(10),
            dni INT,
            telefono VARCHAR(20),
            email VARCHAR(50),
            direccion VARCHAR(50),
            comentarios VARCHAR (100)
);
*/

USE mi_agenda;

SHOW TABLES;

SELECT * FROM agenda_python;
SELECT APELLIDO, NOMBRE_USUARIO FROM agenda_python;
SELECT NOMBRE_USUARIO, TELEFONO FROM agenda_python;
SELECT * FROM agenda_python WHERE NOMBRE_USUARIO = 'Milagros';
--Borrar Tabla agenda_python





            

            
            