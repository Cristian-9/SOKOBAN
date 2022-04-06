class Sokoban:
  #0-Personaje
  #1-Espacio
  #2-Caja
  #3-Pared
  #4-Meta
  #5-Personaje_Meta
  #6-Caja_Meta
   #22meta,caja_meta, personaje
  mapa = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,3,1,1,1,1,3],
    [3,1,1,1,0,1,1,4,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,4,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

  filay = 3 #Posición muñeco en filas
  columnax = 4 #Posición muñeco en columnas

  def imprimirMapa (self):
    print ("***********************************")  
    for fila in self.mapa:
      print(fila)
    print ("***********************************")
    print ()
    
  def moverDerecha (self):
    #Muñeco, Espacio 1
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.columnax += 1
    #Muñeco, Meta 
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 5
      self.columnax += 1
    #muñeco,caja,espacio
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay][self.columnax + 1] = 0 
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
    #personaje,caja,meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #Personaje, Caja_Meta,Espacio
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 5
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #Personaje,Caja_Meta,Meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax + 2] == 4 :
      self.mapa[self.filay][self.columnax] = 1 
      self.mapa[self.filay][self.columnax + 1] = 5 
      self.mapa[self.filay][self.columnax + 2] =  6
      self.columnax += 1
        #Personaje_Meta, Espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 0
      self.columnax += 1
        #Personaje_Meta, Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 4:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5
      self.columnax += 1
      #Personaje_Meta,Caja,Espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay ][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] = 4 
      self.mapa[self.filay][self.columnax + 1] =0 
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
      #Personaje_Meta,Caja,Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] ==4 :
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #personaje_meta,caja_meta,espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax +2] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
      #Prsonaje_Meta,Caja_Meta,Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax +2] == 4:
      self.mapa[self.filay][self.columnax] =4 
      self.mapa[self.filay][self.columnax + 1] =5 
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1 
  
  def moverIzquierda(self):
      #17 espacio, personaje
    if self.mapa[self.filay][self.columnax] == 0 and   self.mapa[self.filay][self.columnax - 1] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 0
      self.columnax -= 1
      #18meta,personaje
    if self.mapa[self.filay][self.columnax] == 0 and   self.mapa[self.filay][self.columnax - 1] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 5
      self.columnax -=1
      
      #19espacio,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay][self.columnax - 2] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 2
      self.columnax -=1
      #20meta,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay][self.columnax -2] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 6
      self.columnax -= 1

      #21espacio,caja_meta,Personaje
    elif self.mapa[self.filay][self.columnax] == 1 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 0:
      self.mapa[self.filay][self.columnax] = 2
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 1
      self.columnax - 1
      #22meta,caja_meta, personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 4:
      self.mapa[self.filay][self.columnax] = 6
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 1
      self.columnax -=1
      #23espacio, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 1 and self.mapa[self.filay][self.columnax - 1] == 5:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 2] = 0
      self.columnax - 1
      #24meta,personaje_meta
      self.mapa[self.filay][self.columnax] == 4 and self.mapa[self.filay][self.columnax -1] == 5
      self.mapa[self.filay][self.columnax] = 5
      self.mapa[self.filay][self.columnax - 2] = 4
      self.columnax - 1
      #25 espacio,caja,personaje_espacio
    elif self.mapa[self.filay][self.columnax] == 1 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay ][self.columnax - 2] == 5:
      self.mapa[self.filay][self.columnax] = 2
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 4
      self.columnax - 1
      #26meta,caja,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 4 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay][self.columnax - 2] == 5:
      self.mapa[self.filay][self.columnax] = 6
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 4
      self.columnax - 1
      #27espacio,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 1 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 5:
      self.mapa[self.filay][self.columnax] = 2
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 4
      self.columnax - 1
      #28meta,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 4 and self.mapa[self.filay][self.columnax - 1] == 5 and self.mapa[self.filay][self.columnax - 2] == 6:
      self.mapa[self.filay][self.columnax] = 6
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 4
      self.columnax - 1
      
  def moverArriba(self):
    #29espacio,personaje
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay-1][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay - 1][self.columnax] = 0
      self.filay -= 1
    #30meta,personaje
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay-1][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] = 5
      self.mapa[self.filay - 1][self.columnax] = 1
      self.filay -= 1
    
      
    
                  
juego = Sokoban()   
juego.imprimirMapa()
while True: #Bucle para jugar N veces
  instrucciones = "Las letras Indican a donde quieres ir\nd-Derecha\na-Izquierda\nw-Arriba"
  print(instrucciones)
  print(juego.filay, ",", juego.columnax)
  movimientos = input("mover a:") #Lee el movimiento del muñeco
  print (juego.filay, juego.columnax)
  if movimientos == "d":
    juego.moverDerecha()
    juego.imprimirMapa()
  elif movimientos == "a":
    juego.moverIzquierda()
    juego.imprimirMapa()
  elif movimientos =="w":
    juego.moverArriba()
    juego.imprimirMapa()
    
      