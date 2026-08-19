#!/usr/bin/env python3
# Version 5: servidor privado del laboratorio primero,
# Internet despues y respaldo local al final.

import ftplib

# Cada servidor: (etiqueta nuestra, host, puerto, carpeta)
SERVIDORES = [
    ("laboratorio", "172.16.10.2", 21, "/pub"),
    ("gnu", "ftp.gnu.org", 21, "/pub"),
    ("local", "127.0.0.1", 2121, "/pub"),
]

def probar_servidor(nombre, host, puerto, carpeta):
    print("=" * 50)
    print(f"*  Servidor: {nombre} ({host}:{puerto})")
    print("=" * 50)
    ftp = ftplib.FTP()
    ftp.connect(host, puerto, timeout=5)
    ftp.login('anonymous', 'demo@local.com')
    print(f"Saludo del servidor: {ftp.welcome}")
    ftp.cwd(carpeta)
    ftp.dir()                      # LIST: imprime el detalle
    nombres = ftp.nlst()           # NLST: el servidor manda los nombres
    print(f"Total de entradas: {len(nombres)}")
    ftp.quit()

def main():
    for nombre, host, puerto, carpeta in SERVIDORES:
        try:
            probar_servidor(nombre, host, puerto, carpeta)
            print("\nConexión cerrada exitosamente.")
            return
        except Exception as e:
            print(f"Fallo {nombre}: {e} -> pruebo el siguiente.\n")
    print("Recorrido terminado sin exito.")

if __name__ == '__main__':
    main()
