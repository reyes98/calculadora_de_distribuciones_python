#@author sebastian

import calculadora as c
 
class Poisson() :
     #constructor    
    def __init__(self,lamda) :
        
        #Atributos de clase
        self.__lamda=lamda                 
    #---------------------------

    #Getters and setters
    def  getLamda(self) :
        return self.__lamda

    def setLamda(self,valor) :
        self.__lamda = valor   
    #----------------------------------

    #método que retorna la probabilidad de p(X=x)
    def funcionProbabilidad(self, x) :
        
        #formula                   
        
        resultado = (self.__lamda**x)*c.e**(-self.__lamda)/(c.factorial(x))
        
        
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
        return self.__lamda  
    
    def varianza(self) :
        return self.__lamda

    def desviacionEstandar(self) :
    	return self.varianza()**(0.5)
    
    #----------------------------------------------------
