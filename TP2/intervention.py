class Intervention:
    def __init__(self, numero, date, duree, tarifkm, technicien):
        self.__numero=numero,
        self.__date=date,
        self.__duree=duree,
        self.__tarifkm=tarifkm,
        self.__technicien=technicien,
        
        
    def affiche(self):
        print("Informations de l'intervention:")
        print("Numero:"+str(self.__numero))
        print("Date:"+str(self.__date))
        print("Duree:"+str(self.__duree))
        print("Tarif en km:"+str(self.__tarifkm))
        print("Technicien:"+str(self.__technicien))
    
    def fraiskm(self,dist):
        frais=self.__tarifkm*dist
        return frais
    
    def fraisMo(self):
        return
    
    