import time
import os

tiempo_trabajo = 25 * 60  # 25 minutos
tiempo_descanso = 5 * 60  # 5 minutos

def cuenta_regresiva(tiempo):
    while tiempo:
        minutos, segundos = divmod(tiempo, 60)
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)
        print(temporizador, end="\r")
        time.sleep(1)
        tiempo -= 1

def notificacion():
    # Para Windows
    # frecuencia = 2500  # Frecuencia en Hz
    # duracion = 1000    # Duración en ms
    # winsound.Beep(frecuencia, duracion)
    
    # Para macOS
    os.system('say "Tiempo terminado"')
    
ciclos = 4  # Número de ciclos Pomodoro

for i in range(ciclos):
    print(f"Ciclo {i+1} de {ciclos} - ¡Hora de concentrarse!")
    cuenta_regresiva(tiempo_trabajo)
    notificacion()
    if i < ciclos - 1:
        print("¡Bien hecho! Ahora toma un descanso.")
        cuenta_regresiva(tiempo_descanso)
        notificacion()
    else:
        print("¡Has completado todos los ciclos! Buen trabajo.")