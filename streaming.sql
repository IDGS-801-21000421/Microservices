CREATE DATABASE streaming;
USE streaming;

CREATE TABLE usuarios(
   id_usuario INT AUTO_INCREMENT PRIMARY KEY,
   nombre VARCHAR(50),
   email VARCHAR(100) UNIQUE,
   password VARCHAR(200)
);

CREATE TABLE videos (
    id_video INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    descripcion TEXT,
    url VARCHAR(250)
);



INSERT INTO usuarios (nombre, email, password) VALUES (
    'Juan Pérez',
    'juan.perez@gmail.com',
    '$2b$12$7uEvfB8iMouUQmWyR8SROe9fkb4uC6r1q5H1rk0GZB2A97waLh.Ey'
);
