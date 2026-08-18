#!/usr/bin/env python3
# Version 4 (main): recorrido multi-servidor con tolerancia a fallos.
import ftplib
import time

SERVIDORES = ['ftp.gwdg.de', 'ftp.ntua.gr']

def listar_servidor(path):
    print("=" * 55)
    print(f"*  Servidor: {path}")
    print("=" * 55)
    t0 = time.perf_counter()
    ftp = ftplib.FTP(host=path, user='anonymous', passwd='nobody@nourl.com')
    print(f"Conexion establecida en {time.perf_counter() - t0:.2f} segundos")
    print(f"Saludo del servidor: {ftp.welcome}")
    try:
        ftp.cwd("/pub")
    except Exception:
        print("Sin /pub disponible, me quedo en la raiz.")
    print(f"Explorando: {ftp.pwd()}")
    nombres = ftp.nlst()
    print(f"Total de entradas en {ftp.pwd()}: {len(nombres)}")
    print("Primeras 8 entradas:")
    for i, nombre in enumerate(nombres[:8], 1):
        print(f"{i:>2}. {nombre}")
    ftp.quit()
    print("Conexion cerrada.")

def principal():
    print("VERSION 4 (main): recorrido multi-servidor")
    for servidor in SERVIDORES:
        try:
            listar_servidor(servidor)
        except Exception as e:
            print(f"Fallo {servidor}: {e} -> pruebo el siguiente.")
    print("\nRecorrido terminado.")

if __name__ == '__main__':
    principal()
