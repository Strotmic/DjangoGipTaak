class Aflos():
    def __init__(self, id,termijn,kapitaal, intrest, schuld):
        self.id = id
        self.termijn = termijn
        self.kapitaal = kapitaal
        self.intrest = intrest
        self.schuld = schuld

    def getId(self):
        return self.id

    def getTermijn(self):
        return self.termijn

    def getKapitaal(self):
        return self.kapitaal

    def getIntrest(self):
        return self.intrest

    def getSchuld(self):
        return self.schuld

class aflosService:  
    def __init__(self,prijs, tijd, rente):
        self.prijs = prijs
        self.tijd = tijd
        self.rente = rente

    def getTabel(self):
        x = []
        voorlopig = self.prijs
        if len(x)> 0:
            x.clear()
        for i in range(self.tijd):
            intrest= voorlopig * self.maandrente()
            kapitaal = self.termijn() - intrest
            schuld = voorlopig - kapitaal
            y = Aflos(i+1,round(self.termijn(),2),round(kapitaal,2),round(intrest,2),round(abs(schuld),2) )
            x.append(y)
            voorlopig = schuld
        return x
    def maandrente(self):
        maandrente = ((1+self.rente)**0.08333333333333333)-1
        return maandrente

    def termijn(self):
        termijn = ((self.prijs*self.maandrente())/(1-((1+self.maandrente())**-self.tijd)))
        return termijn

    def test(self):
        print(self.rente)

#y = Simulatie(3000,0.05,1)
"""x= aflosService(3500,12,0.059)
x.test()
print(x.maandrente())
y = x.getTabel()
for i in range(len(y)):
    print(f"{y[i].getId()} {y[i].getTermijn()} + {y[i].getKapitaal()} + {y[i].getSchuld()} + {y[i].getIntrest()}")"""