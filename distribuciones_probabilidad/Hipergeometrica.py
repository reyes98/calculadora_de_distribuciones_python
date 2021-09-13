#@author sebastian

import calculadora as c
 
class Hipergeometrica() :
     #constructor    
    def __init__(self,r, nTotal,  n) :
        
        #Atributos de clase
        self.__r=r
        self.__nTotal = nTotal
        self.__n = n            
    #---------------------------

    #Getters and setters
    def  getR(self) :
        return self.__r

    def setR(self,valor) :
        self.__r = valor

    def  getNTotal(self) :
        return self.__nTotal

    def setNTotal(self,valor) :
        self.__nTotal = valor    

    def getN(self) :
        return self.__n    

    def setN(self,valor) :
        self.__n = valor    
    #----------------------------------

    #método que retorna la probabilidad de p(X=x)
    def funcionProbabilidad(self, x) :
        
        #formula                   
        resultado = ((c.combinatoria((self.__nTotal-self.__r), (self.__n-x))) * (c.combinatoria(self.__r, x)))/(c.combinatoria(self.__nTotal, self.__n))
        
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
        return (self.__n *self.__r)/self.__nTotal   
    
    def varianza(self) :
        return self.media() * ((self.__nTotal-self.__r)/self.__nTotal) * ((self.__nTotal-self.__n)/(self.__nTotal-1)) 

    def desviacionEstandar(self) :
    	return self.varianza()**(0.5)
    
    #----------------------------------------------------

