class Contrat:
    def __init__(self, numero, date, client, montantContrat, interventions, nbIntervention):
        self.__numero=numero,
        self.__date=date,
        self.__client=client,
        self.__montantContrat=montantContrat,
        self.__interventions=interventions,
        self.nbIntervention=nbIntervention
        
        
    def montant(self):
        return self.__montantContrat
     
     
    def ecart(self):
        return