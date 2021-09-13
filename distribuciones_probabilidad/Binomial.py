#@author sebastian

import calculadora as c
 
class Binomial() :
     #constructor    
    def __init__(self, n,  p) :
        
        #Atributos de clase
        self.__n = n
        self.__p = p            
    #---------------------------

    #Getters and setters
    def  getN(self) :
        return self.__n

    def setN(self,valor) :
        self.__n = valor    

    def getP(self) :
        return self.__p    

    def setP(self,valor) :
        self.__p = valor    
    #----------------------------------

    #método que retorna la probabilidad de p(X=x)
    def funcionProbabilidad(self, x) :
        q = 1 - self.__p
        #formula
        resultado = (c.combinatoria(self.__n, x) * (self.__p**x) * (q**(self.__n - x)))
        
        return resultado
    
    #------------------------------------------------

    #Método que retorna la probabilidad acumulada en un intervalo
    def funcionDistribucion(self, i,  f) :
        resultado = 0.0

        for x in range(i,f+1):
            resultado = resultado + self.funcionProbabilidad(x)                   

        return resultado    
    #---------------------------------------

    #Indicadores    
    def media(self) :
        return self.__n *self.__p   
    
    def varianza(self) :
        return self.media() * (1 - self.__p) 

    def desviacionEstandar(self) :
    	return self.varianza()**(0.5)
    
    #----------------------------------------------------
