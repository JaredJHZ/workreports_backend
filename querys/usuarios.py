usuarios = {
    "insertar":"INSERT INTO usuarios (\"id\", \"usuario\", \"password\",\"privilegios\") VALUES(%s, %s, %s, %s)",
    "consultar_usuario": "SELECT * FROM usuarios WHERE id = %s",
    
}