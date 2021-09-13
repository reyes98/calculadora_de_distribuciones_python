#@author sebastian

import calculadora as c
 
class Bernoulli() :
     #constructor    
    def __init__(self,  p) :
        
        #Atributos de clase        
        self.__p = p            
    #---------------------------

    #Getters and setters
    def getP(self) :
        return self.__p    

    def setP(self,valor) :
        self.__p = valor    
    #----------------------------------

    #método que retorna la probabilidad de p(X=x)
    def funcionProbabilidad(self, x) :
        q = 1 - self.__p
        #formula
        resultado = (self.__p**x) * (q**(1 - x))
        
        return resultado
    
    #------------------------------------------------


    #Indicadores    
    def media(self) :
        return self.__p   
    
    def varianza(self) :
        return self.media() * (1 - self.__p) 

    def desviacionEstandar(self) :
    	return self.varianza()**(0.5)
    
    #----------------------------------------------------
