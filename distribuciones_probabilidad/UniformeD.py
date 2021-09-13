#@author sebastian
 
class UnifromeD() :
     #constructor    
    def __init__(self,n) :
        
        #Atributos de clase
        self.__n=n                 
    #---------------------------

    #Getters and setters
    def  getN(self) :
        return self.__n

    def setN(self,valor) :
        self.__n = valor   
    #----------------------------------

    #método que retorna la probabilidad de p(X=x)
    def funcionProbabilidad(self, x) :
        
        #formula                   
        
        resultado = 1/(self.__n)
        
        
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
        acumulador=0
        for x in range(1,self.__n):
            acumulador+=  x
        return (1/self.__n)*acumulador  
    
    def varianza(self) :
        acumulador=0
        for x in range(1,self.__n):
            acumulador+= (x-self.media())**2
        return (1/self.__n)*acumulador 

    def desviacionEstandar(self) :
        return self.varianza()**(0.5)
    
    #----------------------------------------------------
