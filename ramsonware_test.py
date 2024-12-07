import os
from cryptography.fernet import Fernet

# Generar una clave de cifrado


def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
    return key

# Cargar la clave de cifrado


def load_key():
    return open("encryption.key", "rb").read()

# Cifrar archivos


def encrypt_files(key, directory):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    data = f.read()
                encrypted_data = fernet.encrypt(data)
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)
                print(f"Archivo cifrado: {file_path}")
            except Exception as e:
                print(f"Error al cifrar {file_path}: {e}")

# Decifrar archivos


def decrypt_files(key, directory):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    encrypted_data = f.read()
                data = fernet.decrypt(encrypted_data)
                with open(file_path, "wb") as f:
                    f.write(data)
                print(f"Archivo descifrado: {file_path}")
            except Exception as e:
                print(f"Error al descifrar {file_path}: {e}")


# Programa principal
if __name__ == "__main__":
    print("Este programa es solo para fines educativos.")
    option = input("¿Deseas cifrar (E) o descifrar (D) archivos? ")
    directory = input("Ingresa el directorio donde están los archivos: ")

    if option.lower() == "e":
        key = generate_key()
        encrypt_files(key, directory)
        print("Los archivos han sido cifrados. Guarda la clave en 'encryption.key' para descifrarlos.")
    elif option.lower() == "d":
        key = load_key()
        decrypt_files(key, directory)
        print("Los archivos han sido descifrados.")
    else:
        print("Opción no válida.")
