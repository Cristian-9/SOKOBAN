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
    print ("***************************")  
    for fila in self.map:
      print(fila)
    print ("***************************")
    print ()
    
  def moverDerecha (self):
    #Muñeco, Espacio
    if self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax + 1] == 1:
      self.map[self.filay][self.columnax] = 1
      self.map[self.filay][self.columnax + 1] = 0
      self.columnax += 1
    #Muñeco, Meta
    elif self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax] == 4:
      self.map[self.filay][self.columnax] = 1
      self.map[self.filay][self.columnax + 1] = 5
      self.posx += 1
    #Muñeco, Caja, Espacio
    elif self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] == 1:
      self.map[self.filay][self.columnax] = 1
      self.map[self.filay][self.columnax + 1] = 0
      self.map[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #Personaje, Caja, Meta
    elif self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] == 4:
      self.map[self.filay][self.columnax] = 1
      self.map[self.filay][self.columnax + 1] = 0
      self.map[self.filay][self.columnax + 2] = 5
      self.columnax += 1
      #Personaje, Caja_Meta,Espacio
    elif self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax + 1] == 6 and self.map[self.filay + 2] == 1 :
          self.map[self.filay][self.columnax] = 1
          self.map[self.filay][self.columnax + 1] = 5 
          self.map[self.filay][self.columnax + 2] = 2
          self.columnax += 1
      #Personaje,Caja_Meta,Meta
    elif self.map[self.filay][self.columnax] == 0 and self.map[self.filay][self.columnax + 1] == 6 and self.map[self.filay + 2] == 4 :
      self.map[self.filay][self.columnax] = 1 
      self.map[self.filay][self.columnax + 1] = 5 
      self.map[self.filay][self.columnax + 2] =  6
      self.columnax += 1
      #Personaje_Meta, Espacio
    if self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 1:
      self.map[self.filay][self.columnax] = 0
      self.map[self.filay][self.columnax + 1] = 4 
      self.columnax += 1     
      #Personaje_Meta, Meta
    if self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 4 :
      self.map[self.filay][self.columnax] = 4
      self.map[self.filay][self.columnax + 1] = 5 
      self.columnax += 1
      #Personaje_Meta,Caja,Espacio
    elif self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] == 1:
      self.map[self.filay][self.columnax] = 4 
      self.map[self.filay][self.columnax + 1] =0 
      self.map[self.filay][self.columnax + 2] = 2
      self.columnax += 1 
      #Personaje_Meta,Caja,Meta
    elif self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 2 and self.map[self.filay + 2] ==4 :
      self.map[self.filay][self.columnax] = 4
      self.map[self.filay][self.columnax + 1] = 0
      self.map[self.filay][self.columnax + 2] = 6
      self.columnax += 1 
    elif self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 6 and self.map[self.filay + 2] == 1:
      self.map[self.filay][self.columnax] = 4
      self.map[self.filay][self.columnax + 1] = 5
      self.map[self.filay][self.columnax + 2] = 2
      self.columnax += 1 
      #Prsonaje_Meta,Caja_Meta,Meta
    elif self.map[self.filay][self.columnax] == 5 and self.map[self.filay][self.columnax + 1] == 6 and self.map[self.filay + 2] == 4:
      self.map[self.filay][self.columnax] =4 
      self.map[self.filay][self.columnax + 1] =5 
      self.map[self.filay][self.columnax + 2] = 6
      self.columnax += 1 
      
juego = Sokoban()

juego.imprimirMapa()

while True: #Bucle para jugar N veces
  instrucciones = "Las letras Indican a donde quieres ir\nd-Derecha\na-Izquierda\n"
  print(instrucciones)
  movimientos = input(":") #Lee el movimiento del muñeco
  if movimientos == "d": #Si es d - moverá a la derecha
    juego.moverDerecha()
    juego.imprimirMapa()