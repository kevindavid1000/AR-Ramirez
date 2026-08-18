#!/usr/bin/env python3
# RAMA Nueva_Funcion: banner, saludo, cronometro, conteo y arbol limitado.
import ftplib
import time

FTP_SERVER_URL = 'ftp.freebsd.org'
MAX_PROFUNDIDAD = 2    # niveles bajo la raiz: no vamos a crawlear el mirror entero
MAX_DIRECTORIOS = 12   # tope de directorios visitados: ser buen huesped

def imprimir_arbol(ftp, profundidad, prefijo, contador):
    """Imprime el arbol del directorio actual; recursion limitada."""
    if profundidad > MAX_PROFUNDIDAD:
        return
    try:
        nombres = ftp.nlst()
    except Exception:
        return
    for i, nombre in enumerate(nombres):
        ultimo = (i == len(nombres) - 1)
        conector = "└── " if ultimo else "├── "
        es_dir = False
        if profundidad < MAX_PROFUNDIDAD and contador[0] < MAX_DIRECTORIOS:
            try:
                ftp.cwd(nombre)   # si puede entrar, es directorio
                es_dir = True
            except Exception:
                es_dir = False
        print(prefijo + conector + nombre + ("/" if es_dir else ""))
        if es_dir:
            contador[0] += 1
            rama = "    " if ultimo else "│   "
            imprimir_arbol(ftp, profundidad + 1, prefijo + rama, contador)
            ftp.cwd("..")         # regresar al padre

def test_ftp_connection(path, username, email):
    try:
        print("=" * 50)
        print("*  RAMA nueva-funcion: VERSION DE PRUEBA  *")
        print("=" * 50)
        t0 = time.perf_counter()
        ftp = ftplib.FTP(host=path, user=username, passwd=email)
        print(f"\nConexion establecida en {time.perf_counter() - t0:.2f} segundos")
        print(f"Saludo del servidor: {ftp.welcome}")
        ftp.cwd("/")
        print(f"Directorio actual en el servidor: {ftp.pwd()}")
        print("\nArbol del servidor (limitado):")
        contador = [0]
        imprimir_arbol(ftp, 0, "", contador)
        nombres = ftp.nlst()
        print(f"\nTotal de entradas en la raiz: {len(nombres)}")
        ftp.quit()
        print("\nConexión cerrada exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al conectar o listar los archivos: {e}")

if __name__ == '__main__':
    test_ftp_connection(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')
