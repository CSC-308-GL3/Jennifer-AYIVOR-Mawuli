class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.__numero=numero,
        self.__nom=nom,
        self.__qualification=qualification,
        self.__dateEmbauche=dateEmbauche
        
        

    def coutHoraire(self):
        return
    
    
    def getNumero(self):
        return self.__numero
    
    def getNom(self):
        return self.__nom
    
    def getQualification(self):
        return self.__qualification
    
    def getDateEmbauche(self):
        return self.__dateEmbauche
    
    def getAncienete(self):
        return 