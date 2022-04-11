from os import system, name
class Sokoban:
  mapa = []
  filay = 0
  columnax = 0
  nivel = ()
  completo = False
  def crearMapa(self):
    for i in self.abrirNivel:
      linea = []
      for digito in i:
        if digito == "\n":
          continue
        linea.append(int(digito))
      self.mapa.append(linea)
  def imprimirMapa(self):
      for fila in self.mapa:
          for i in fila:
              if i == 0:
                  print(chr(128520), end="")
              elif i == 1:
                  print("  ", end="")
              elif i == 2:
                  print(chr(128230), end= "")
              elif i == 3:
                  print(chr(128679), end="")
              elif i == 4:
                  print(chr(127937), end="")
              elif i == 5:
                  print(chr(129430), end="")
              elif i == 6:
                  print(chr(128081), end="")
              else:
                  print(i, end="")
          print()
        
  def encontraPersonaje( self ):
    for  fila  in  range(len(self. mapa)): 
      for  columna in  range (len(self.mapa[fila])): 
        if self.mapa[fila][columna] ==  0 : 
          self.filay  =  fila                       
          self.columnax =  columna 
  def evaluarMapa(self):
        verificador = []
        for linea in self.mapa:
            num2 = linea.count(4)
            verificador.append(num2)
        if sum(verificador) == 0:
            self.limpiarPantalla()
            print('¡EL NIVEL ESTA COMPLETO!')
            self.completo = True
        else:
            pass        
  def limpiarPantalla(self):
      if name == "int":
          system('cls')#windows
      else:
        system('clear')
  def moverDerecha (self):
    #5Muñeco, Espacio 
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
      #33espacio,caja_meta,personaje
    elif self.mapa[self.filay][self.columnax] == 0 and self.mapa[self.filay - 1][self.columnax] == 6 and self.mapa[self.filay - 2][self.columnax] == 1:
      self.mapa[self.filay][self.columnax] = 1
      self.mapa[self.filay - 1][self.columnax] = 5
      self.mapa[self.filay - 2][self.columnax] = 2
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
  def comenzarJuego(self):
      print('Bienvenido \nActualmente el juego cuenta con 4 niveles')
      comienza = False
      while comienza == False:
          nuevo = input('¿Qué nivel desea abrir? \n\t 1 ° 2 ° 3 °4 \n: ')
          if nuevo == '1':
              self.abrirNivel = open("Danilv0.txt", "r")
              comienza = True
          elif nuevo == '2':
              self.abrirNivel = open("Danilv1.txt", "r")
              comienza = True
          elif nuevo == '3':
              self.abrirNivel = open("Danilv2.txt", "r")
              comienza = True
          elif nuevo == '4':
              self.abrirNivel = open("Danilv3.txt", "r")
              comienza = True
          else:
            self.limpiarPantalla()
            print("El juego solo tiene 4 niveles")
      self.limpiarPantalla()
      self.crearMapa()
      self.encontraPersonaje()
      self.imprimirMapa()

      while self.completo == False:
            instrucciones = "Las letras Indican a donde quieres ir\nd-Derecha\na-Izquierda\nw-Arriba\nq-Termina el Juego"
            print(instrucciones)
            print("Posición: ", "[", self.filay, ",", self.columnax, "]")
            movimiento = input('Movimiento: ')
            if movimiento == "w":
                self.moverArriba()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 's':
                self.moverAbajo()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 'd':
                self.moverDerecha()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            elif movimiento == 'a':
                self.moverIzquierda()
                self.limpiarPantalla()
                self.imprimirMapa()
                self.evaluarMapa()
            else:
                self.limpiarPantalla()
                print("Saliste del Juego")
                break
                
juego = Sokoban()
juego.comenzarJuego()
continua = input('¿Deseas continuar? \n\ts/n\n:')
juego.limpiarPantalla()
while continua == 's':
    juego.completo = False
    juego.comenzarJuego()
    juego.limpiarPantalla()
else:
  print("Juego terminado\n¡¡Gracias por Jugar!!")