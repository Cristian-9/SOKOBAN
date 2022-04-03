class Sokoban:
  #0-Personaje
  #1-Espacio
  #2-Caja
  #3-Pared
  #4-Meta
  #5-Personaje_Meta
  #6-Caja_Meta
  mapa = [
    [3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,3],
    [3,1,4,1,0,1,1,4,3],
    [3,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3]
]

  filay = 2 #Posición muñeco en filas
  columnax = 4 #Posición muñeco en columnas

  def __init__ (self):
    print ("Sokoban v0.2 by Cristian-9 \n\n")

  def imprimirMapa (self):
    print ("***************************")  
    for fila in self.mapa:
      print(fila)
    print ("***************************")
    print ()
    
  def moverDerecha (self):
    #Muñeco, Espacio 1
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.columnax += 1
    #Muñeco, Meta 2
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 5
      self.columnax + 1
    #Muñeco, Caja, Espacio 3
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay + 2] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #Personaje, Caja, Meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay + 2] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 5
      self.columnax += 1
      #Personaje, Caja_Meta,Espacio
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.map[self.filay + 2] == 1 :
          self.mapa[self.filay][self.columnax] = 1
          self.mapa[self.filay][self.columnax + 1] = 5 
          self.map[self.filay][self.columnax + 2] = 2
          self.columnax += 1
      #Personaje,Caja_Meta,Meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay + 2] == 4 :
      self.mapa[self.filay][self.columnax] = 1 
      self.mapa[self.filay][self.columnax + 1] = 5 
      self.mapa[self.filay][self.columnax + 2] =  6
      self.columnax += 1
      #Personaje_Meta, Espacio
    if self.mapa[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 0
      self.mapa[self.filay][self.columnax + 1] = 4 
      self.columnax += 1     
      #Personaje_Meta, Meta
    if self.mapa[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 4 :
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5 
      self.columnax += 1
      #Personaje_Meta,Caja,Espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] == 1:
      self.mapa[self.filay][self.columnax] = 4 
      self.mapa[self.filay][self.columnax + 1] =0 
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1 
      #Personaje_Meta,Caja,Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] ==4 :
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1 
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay + 2] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1 
      #Prsonaje_Meta,Caja_Meta,Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay + 2] == 4:
      self.mapa[self.filay][self.columnax] =4 
      self.mapa[self.filay][self.columnax + 1] =5 
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1 
    juego = Sokoban()     
  
  def moverIzquierda(self):
      #espacio, personaje
    if self.mapa[self.filay][self.columnax] == 0 and   self.mapa[self.filay][self.columnax - 1] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 0
      self.columnax -= 1
      #meta,personaje
    elif self.mapa[self.filay][self.columnax] == 4 and self.mapa[self.filay][self.columnax + 1] == 0:
      self.mapa[self.filay][self.columnax] = 5
      self.mapa[self.filay][self.columnax + 1] = 1
      self.columnax + 1
      #espacio,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 1 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay - 2] == 0:
      self.mapa[self.filay][self.columnax] = 6 
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 1
      self.columnax - 1
      #meta,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 4 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay - 2] == 0:
      self.mapa[self.filay][self.columnax] = 5
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 1
      self.columnax - 1
juego = Sokoban()   
juego.imprimirMapa()
while True: #Bucle para jugar N veces
  instrucciones = "Las letras Indican a donde quieres ir\nd-Derecha\na-Izquierda\n"
  print(instrucciones)
  movimientos = input("mover a:") #Lee el movimiento del muñeco
  if movimientos == "d":
    juego.moverDerecha()
    juego.imprimirMapa()
  elif movimientos == "a":
    juego.moverIzquierda()
    juego.imprimirMapa()
    
      