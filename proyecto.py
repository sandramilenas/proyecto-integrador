import random

# Constantes

LADO = 10
PARED = '#'
PASILLO = '.'
PERSONAJE = 'P'

# Funciones

def generar_laberinto():
  """Genera un laberinto de LADO x LADO."""
  laberinto = [[PARED for _ in range(LADO)] for _ in range(LADO)]

  # Generamos las paredes
  for i in range(LADO):
    laberinto[0][i] = PARED
    laberinto[LADO - 1][i] = PARED
    laberinto[i][0] = PARED
    laberinto[i][LADO - 1] = PARED

  # Generamos los pasillos
  for i in range(1, LADO - 1):
    for j in range(1, LADO - 1):
      if random.randint(0, 1):
        laberinto[i][j] = PASILLO

  # Colocamos al personaje
  laberinto[0][0] = PERSONAJE

  return laberinto

def imprimir_laberinto(laberinto):
  """Imprime un laberinto en pantalla."""
  for fila in laberinto:
    print(''.join(fila))

def mover_personaje(laberinto, tecla):
  """Mueve al personaje en la dirección indicada por la tecla."""
  x, y = get_posicion_personaje(laberinto)

  if tecla == 'w':
    y -= 1
  elif tecla == 's':
    y += 1
  elif tecla == 'a':
    x -= 1
  elif tecla == 'd':
    x += 1

  # Comprobamos que la nueva posición es válida
  if 0 <= x < LADO and 0 <= y < LADO and laberinto[x][y] == PASILLO:
    laberinto[x][y] = PERSONAJE
    laberinto[y][x] = PERSONAJE

def get_posicion_personaje(laberinto):
  """Devuelve la posición del personaje en el laberinto."""
  for i in range(LADO):
    for j in range(LADO):
      if laberinto[i][j] == PERSONAJE:
        return i, j

def main():
  """Ejecuta el juego."""
  laberinto = generar_laberinto()
  imprimir_laberinto(laberinto)

  while True:
    tecla = input('Introduce una tecla: ')
    mover_personaje(laberinto, tecla)
    imprimir_laberinto(laberinto)

if __name__ == '__main__':
  main()