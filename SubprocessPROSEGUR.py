import datetime
import os
import subprocess
#Definir funcion que codifique los dias de la semana
def es_dia_habil(fecha):
    return 0 <= fecha.weekday() <= 4  # Martes (1) a viernes (4)

# Obtener la fecha actual
fecha_actual = datetime.datetime.now()

if es_dia_habil(fecha_actual):
    def execute_lnk(lnk_path):
        try:
            # Verificar que la ruta del archivo .lnk existe
            if not os.path.exists(lnk_path):
                raise FileNotFoundError("El archivo .lnk no existe.")

            # Utilizar 'start' en Windows para abrir el destino del acceso directo
            subprocess.Popen(['start', '', lnk_path], shell=True)

        except Exception as e:
            print("Error:", e)
    # Ejemplo de uso
    if fecha_actual.weekday() == 0:  # Si es lunes
        lnk_file_path = "C:\\Users\\alan.riquelmes\\Desktop\\ProsegurLunes.lnk"
    else:
        lnk_file_path = "C:\\Users\\alan.riquelmes\\Desktop\\Prosegur.lnk"

    execute_lnk(lnk_file_path)
    print("Ejecutando el código en días hábiles...")

else:
    print("Hoy no es un día hábil.")
