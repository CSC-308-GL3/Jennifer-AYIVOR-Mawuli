class Navire:
    def __init__(self,noNavire, nomNavire, libelleFret, qteFret):
        self.__noNavire=noNavire,
        self.__nomNavire=nomNavire,
        self.__libelleFret=libelleFret,
        self.__qteFret=qteFret
        
    #fonction obtenirQteFret
    def obtenirQteFret(self):
        return self.__qteFret
    
    #fonction decharger
    def decharger(self,qte):
        self.__qteFret-=qte
    
    #fonction estDecharge    
    def estDecharge(self):
        return self.__qteFret==0
    