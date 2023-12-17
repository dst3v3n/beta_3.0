import bcrypt

def encriptar (Contraseña:str):
    password = Contraseña.encode('utf-8')
    salt = b'$2b$12$tO6x66Zxi6sn6THHX/M.A.'
    hashed = bcrypt.hashpw(password, salt)
    return str(hashed)