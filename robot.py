'''
Aca tenemos a HAL
'''
from estrategia import Estrategia
from ambiente import Ambiente

class Robot():
    '''
    '''
    def __init__(self, orientacion, posicion, estrategia, ambiente):
        '''
		Inicializa el objeto Robot con su posicion, orientacion y un objeto estrategia asociado
        '''
		self.mi_ambiente = ambiente        
		self.giroscopo = orientacion
        self.posicion = posicion
        self.historia_posiciones = []
        self.historia_acciones = []
        # asumo que estrategia fue inicializada por el main
		self.mi_estrategia = estrategia

    def rotar(self, giro):
        '''
		Recibe un int giro de estrategia y actualiza la orientacion del giroscopo
		Sin retorno, solo actualiza la orientacion, en grados
        '''
		self.giroscopo += giro
		# mantengo a giroscopo entre 0 y 360 grados
		if self.giroscopo >= 360:
			self.giroscopo -= 360
		if self.giroscopo < 0:
			self.giroscopo += 360 
        self.historia_acciones.append(self.giroscopo)

    def mover(self, pasos):
         '''
        Esto usa la estrategia para una rapida solucion
		Sin retorno, actualiza la posicion del objeto
		Quizas deba agregar un chequeo de las orientaciones y de la poscion dentro del ambiente
         '''
        if self.giroscopos == 0:
			self.posicion[0] += pasos
		elif self.giroscopo == 90:
 			self.posicion[1] -= pasos
		elif self.giroscopo[] == 180:
			self.posicion[0] += pasos
		elif self.giroscopo[] == 360:
			self.posicion[1] -= pasos
		self.historia_acciones.append(self.posicion)
		self.historia_posiciones.appende(self.posicion)

    def sensar(self):
         '''
        SOLO sensa para adelante y toma de ambientes la distancia al proximo obstaculo o limite en la orientacion actual	
		Devuelve el numero entero de pasos posibles hacia adelante
         '''
		return = self.ambiente.eco(self.posicion, self.orientacion
		
    def proximo_paso(self):
        '''
        Envia estado actual a estrategia para recibir una orden. Estrategia ejecutara las funciones mover, sensar y girar
        '''
		self.mi_estrategia.decidir(posicion, giroscopo, historia_posiciones, historia_acciones)
        
