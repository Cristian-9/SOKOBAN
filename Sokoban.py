class Sokoban:
  #0-Personajed
  #1-Espacio
  #2-Caja
  #3-Pared
  #4-Meta
  #5-Personaje_Meta
  #6-Caja_Meta
   #22meta,caja_meta, personaje
  mapa = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,4,3],
    [3,1,1,1,1,1,1,1,1,2,1,1,1,3],
    [3,4,1,1,2,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,0,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

  filay = 6 #Posición muñeco en filas
  columnax = 1 #Posición muñeco en columnas

  def imprimirMapa (self):  
    for fila in self.mapa:
      for i in self.mapa:
        print(str(i)
            .replace(',','')
            .replace('0','😈')
            .replace('1', '  ')
            .replace('2','📦')
            .replace('3','🚧')
            .replace('4','🏁')
            .replace('5','🛐')
            .replace('6','👑')
            .replace('[','')
            .replace(']',''))
      print(fila)
    print ("***********************************")
    print ()
    
  def moverDerecha (self):
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.columnax += 1
    #6Muñeco, Meta 
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 5
      self.columnax += 1
    #7muñeco,caja,espacio
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay][self.columnax + 1] = 0 
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
    #8personaje,caja,meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #9Personaje, Caja_Meta,Espacio
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax + 1] = 5
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #10Personaje,Caja_Meta,Meta
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax + 2] == 4 :
      self.mapa[self.filay][self.columnax] = 1 
      self.mapa[self.filay][self.columnax + 1] = 5 
      self.mapa[self.filay][self.columnax + 2] =  6
      self.columnax += 1
      #11Personaje_Meta, Espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 0
      self.columnax += 1
      #12Personaje_Meta, Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 4:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5
      self.columnax += 1
      #13Personaje_Meta,Caja,Espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay ][self.columnax + 2] == 1:
      self.mapa[self.filay][self.columnax] = 4 
      self.mapa[self.filay][self.columnax + 1] =0 
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
      #14Personaje_Meta,Caja,Meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 2 and self.mapa[self.filay][self.columnax + 2] ==4 :
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 0
      self.mapa[self.filay][self.columnax + 2] = 6
      self.columnax += 1
      #15personaje_meta,caja_meta,espacio
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax + 1] == 6 and self.mapa[self.filay][self.columnax +2] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax + 1] = 5
      self.mapa[self.filay][self.columnax + 2] = 2
      self.columnax += 1
      #16Personaje_Meta,Caja_Meta,Meta
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
    elif self.mapa[self.filay][self.columnax] == 0 and   self.mapa[self.filay][self.columnax - 1] == 4:
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
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 2
      self.columnax -= 1
      #22meta,caja_meta, personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 6
      self.columnax -=1
      #23espacio, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax - 1] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 0
      self.columnax -= 1
      #24meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax -1] == 4:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 5
      self.columnax -= 1
      #25 espacio,caja,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay ][self.columnax - 2] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 2
      self.columnax -= 1
      #26meta,caja,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax - 1] == 2 and self.mapa[self.filay][self.columnax - 2] == 4:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 0
      self.mapa[self.filay][self.columnax - 2] = 6
      self.columnax -= 1
      #27espacio,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 2
      self.columnax -= 1
      #28meta,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay][self.columnax - 1] == 6 and self.mapa[self.filay][self.columnax - 2] == 4:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay][self.columnax - 1] = 5
      self.mapa[self.filay][self.columnax - 2] = 6
      self.columnax -= 1

  def moverArriba(self):
     #29espacio,personaje
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay-1][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay - 1][self.columnax] = 0
      self.filay -= 1
    #30meta,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay-1][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay - 1][self.columnax] = 5
      self.filay -= 1
      #31espacio,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay - 1][self.columnax] == 2 and self.mapa[self.filay - 2][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay - 1][self.columnax] = 0 
      self.mapa[self.filay - 2][self.columnax] = 2
      self.filay -=1
      #32meta,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay - 1][self.columnax] == 2 and self.mapa[self.filay - 2][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay - 1][self.columnax] = 0 
      self.mapa[self.filay - 2][self.columnax] = 6
      self.filay -=1
      #34meta,caja_meta, personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay - 1][self.columnax] == 6 and self.mapa[self.filay - 2][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay - 1][self.columnax] = 5
      self.mapa[self.filay - 2][self.columnax] = 6
      self.filay -=1
      #35espacio, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay - 1][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay -1][self.columnax] = 0
      self.filay -=1
      #36meta, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay - 1][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4
        self.mapa[self.filay -1][self.columnax] = 5
        self.filay -=1
      #37espacio,caja, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay -1][self.columnax] == 2 and self.mapa[self.filay -2][self.columnax] == 1:
        self.mapa[self.filay ][self.columnax] =4  
        self.mapa[self.filay - 1][self.columnax]= 0
        self.mapa[self.filay - 2][self.columnax] = 2
        self.filay -=1
      #38meta,caja,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay - 1][self.columnax] == 2 and self.mapa[self.filay - 2][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay - 1][self.columnax] = 0
        self.mapa[self.filay - 2][self.columnax] = 6
        self.filay -=1
      #39espacio, caja_meta,personaje_meta   
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay - 1][self.columnax] == 6 and self.mapa[self.filay - 2][self.columnax] == 1:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay - 1][self.columnax] = 5
        self.mapa[self.filay - 2][self.columnax] = 2
        self.filay -=1
      #40meta,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay - 1][self.columnax] == 6 and self.mapa[self.filay - 2][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay - 1][self.columnax] = 5
        self.mapa[self.filay - 2][self.columnax] = 6
        self.filay -=1
  def moverAbajo(self):
#41espacio,personaje
    if self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay + 1][self.columnax] = 0
      self.filay += 1
    #42meta,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay + 1][self.columnax] = 5
      self.filay += 1
    #43espacio,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 2 and self.mapa[self.filay + 2][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay + 1][self.columnax] = 0 
      self.mapa[self.filay + 2][self.columnax] = 2
      self.filay +=1
      #4meta,caja,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 2 and self.mapa[self.filay + 2][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay + 1][self.columnax] = 0 
      self.mapa[self.filay + 2][self.columnax] = 6
      self.filay +=1
     #45espacio,caja_meta,Personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 6 and self.mapa[self.filay + 2][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay + 1][self.columnax] = 5
      self.mapa[self.filay + 2][self.columnax] = 2
      self.filay +=1 
    #46meta,caja_meta, personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay + 1][self.columnax] == 6 and self.mapa[self.filay + 2][self.columnax] == 4:
      self.mapa[self.filay][self.columnax] =  1
      self.mapa[self.filay + 1][self.columnax] = 5
      self.mapa[self.filay + 2][self.columnax] = 6
      self.filay +=1
      #47espacio, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay + 1][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 4
      self.mapa[self.filay +1][self.columnax] = 0
      self.filay +=1
      #48meta, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay + 1][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4
        self.mapa[self.filay + 1][self.columnax] = 5
        self.filay +=1
      #49espacio,caja, personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay +1][self.columnax] == 2 and self.mapa[self.filay +2][self.columnax] == 1:
        self.mapa[self.filay ][self.columnax] =4  
        self.mapa[self.filay + 1][self.columnax]= 0
        self.mapa[self.filay + 2][self.columnax] = 2
        self.filay +=1
       #50meta,caja,personaje_meta     
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay + 1][self.columnax] == 2 and self.mapa[self.filay + 2][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay + 1][self.columnax] = 0
        self.mapa[self.filay + 2][self.columnax] = 6
        self.filay +=1   
      #51espacio, caja_meta,personaje_meta   
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay + 1][self.columnax] == 6 and self.mapa[self.filay + 2][self.columnax] == 1:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay + 1][self.columnax] = 5
        self.mapa[self.filay + 2][self.columnax] = 2
        self.filay +=1
      #52meta,caja_meta,personaje_meta
    elif self.mapa[self.filay][self.columnax] == 5 and self.mapa[self.filay + 1][self.columnax] == 6 and self.mapa[self.filay + 2][self.columnax] == 4:
        self.mapa[self.filay][self.columnax] = 4 
        self.mapa[self.filay + 1][self.columnax] = 5
        self.mapa[self.filay + 2][self.columnax] = 6
        self.filay +=1
      
juego = Sokoban()   
juego.imprimirMapa()
while True: #Bucle para jugar N veces
  print (juego.filay, juego.columnax)
  instrucciones = "Las letras Indican a donde quieres ir\nd-Derecha\na-Izquierda\nw-Arriba"
  print(instrucciones)
  print(juego.filay, ",", juego.columnax)
  movimientos = input("mover a:") #Lee el movimiento del muñeco
  if movimientos == "d":
    juego.moverDerecha()
    juego.imprimirMapa()
  elif movimientos == "a":
    juego.moverIzquierda()
    juego.imprimirMapa()
  elif movimientos =="w":
    juego.moverArriba()
    juego.imprimirMapa()
  elif movimientos  =="s":
    juego.moverAbajo()
    juego.imprimirMapa()
    
      