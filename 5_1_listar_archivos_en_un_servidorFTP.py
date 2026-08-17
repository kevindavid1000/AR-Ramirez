#!/usr/bin/env python3
# Python Network Programming Cookbook -- Chapter - 5
# Codigo migrado de Python 2.7 a Python 3.12+ (compatible con 3.14)

import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'

def test_ftp_connection(path, username, email):
    try:
        # Abrir conexion FTP (usuario anonimo)
        ftp = ftplib.FTP(host=path, user=username, passwd=email)

        # Entrar a la carpeta /pub
        ftp.cwd("/pub")

        # Listar los archivos
        print(f"File list at {path}:")
        ftp.dir()

        # Cerrar conexion
        ftp.quit()
        print("\nConexión cerrada exitosamente.")

    except Exception as e:
        print(f"Ocurrió un error al conectar o listar los archivos: {e}")

if __name__ == '__main__':
    test_ftp_connection(
        path=FTP_SERVER_URL,
        username='anonymous',
        email='nobody@nourl.com'
    )
