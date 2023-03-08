from navire import Navire
from port import Port
from stockage import Stockage

navire = Navire("0092493603", "ESMERALDA", "sac de riz", 1200)

silo1 = Stockage(100,100)
silo2 = Stockage(200,200)
silo3 = Stockage(300,300)

hangar1 = Stockage(1000,500)
hangar2 = Stockage(1000,750)

hangar1.stocker(500)
hangar2.stocker(250)

zonesDeStockage = [silo1, silo2, silo3, hangar1, hangar2]

port = Port(zonesDeStockage)

port.dechargement(navire)

print("La quantité Fret restant : ",navire.obtenirQteFret())