class Sokoban:
  #0-Personaje
  #1-Espacio
  #2-Caja
  #3-Pared
  #4-Meta
  #5-Personaje_Meta
  #6-Caja_Meta
  map = [
    [3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,3],
    [3,1,1,1,0,1,1,1,3],
    [3,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3]
]

  filay = 2 #Posición muñeco en filas
  columnax = 4 #Posición muñeco en columnas

  def __init__ (self):
    print ("Sokoban v0.2 by Cristian-9 \n\n")

  def imprimirMapa (self):
    print ("[][][][[[[][][][][][][][][][][]")  
    for fila in self.map:
      print(fila)
    print ("[][][][[[[][][][][][][][][][][]")
    print ()