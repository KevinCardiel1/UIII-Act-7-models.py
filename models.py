-- ======================================
-- TABLA: Estudiante
-- ======================================
CREATE TABLE Estudiante (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE,
    genero CHAR(1),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100),
    num_matricula VARCHAR(20),
    fecha_inscripcion DATE
);

-- ======================================
-- TABLA: Profesor
-- ======================================
CREATE TABLE Profesor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(20),
    especialidad VARCHAR(100),
    fecha_contratacion DATE,
    salario DECIMAL(10,2),
    dni VARCHAR(20)
);

-- ======================================
-- TABLA: Curso
-- ======================================
CREATE TABLE Curso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100),
    descripcion TEXT,
    creditos INT,
    profesor_id INT,
    horario VARCHAR(100),
    aula VARCHAR(50),
    nivel_educativo VARCHAR(50),
    costo_curso DECIMAL(10,2),
    FOREIGN KEY (profesor_id) REFERENCES Profesor(id)
);

-- ======================================
-- TABLA: Inscripcion
-- ======================================
CREATE TABLE Inscripcion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_inscripcion DATE,
    estado_inscripcion VARCHAR(50),
    nota_final DECIMAL(4,2),
    fecha_modificacion DATETIME,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiante(id),
    FOREIGN KEY (curso_id) REFERENCES Curso(id)
);

-- ======================================
-- TABLA: Asistencia
-- ======================================
CREATE TABLE Asistencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_clase DATE,
    presente BOOLEAN,
    justificacion TEXT,
    comentarios TEXT,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiante(id),
    FOREIGN KEY (curso_id) REFERENCES Curso(id)
);

-- ======================================
-- TABLA: Materia
-- ======================================
CREATE TABLE Materia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_materia VARCHAR(100),
    descripcion TEXT,
    nivel_academico VARCHAR(50),
    es_obligatoria BOOLEAN,
    horas_semanales INT
);

-- ======================================
-- TABLA: Calificacion
-- ======================================
CREATE TABLE Calificacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    inscripcion_id INT,
    tipo_evaluacion VARCHAR(50),
    fecha_evaluacion DATE,
    puntaje DECIMAL(5,2),
    ponderacion DECIMAL(3,2),
    comentarios TEXT,
    FOREIGN KEY (inscripcion_id) REFERENCES Inscripcion(id)
);
