class tempo:
    def __init__(self,orario=None,periodo=0.5):
        self.orario=orario
        self.periodo=periodo

    def approssimazione_al_periodo(self,orario=None):
        approssimazione=int(orario/self.periodo)*self.periodo

        return approssimazione

    def ora_con_min_decimali(self,orario=None):
        h=int(orario)
        min=round(orario*100-(h*100))
        min_decimali=min/60
        ora_con_min_decimali=h+min_decimali
        return ora_con_min_decimali

    def ora_con_min(self,orario=None):
        h=int(orario)
        min_decimali=round(orario*100-(h*100))
        min=min_decimali/100*60
        ora_con_min=h+min/100
        return ora_con_min
    
class tempo_lavoro(tempo):
    def __init__(self,entrata=None,uscita=None):
        super().__init__()
        self.entrata=entrata
        self.uscita=uscita

    def lavorato(self):
        entrata=self.ora_con_min_decimali(self.entrata_valida(self.entrata))
        uscita=self.ora_con_min_decimali(self.uscita_valida(self.uscita))
        # print("entrata e uscita cartellino: "+str(self.entrata )+ " - "+str(self.uscita) )
        # print("entrata e uscita valida: "+ str( entrata )+ " - "+str(uscita) )
        tempo_lavorato= self.ora_con_min(uscita-entrata)
        # print("tempo lavorato: "+str(tempo_lavorato))
        return tempo_lavorato
        

    def entrata_valida(self,orario):
        orario_decimale=self.ora_con_min_decimali(orario)
        orario_al_periodo=self.approssimazione_al_periodo(orario_decimale)
        if orario_decimale <= orario_al_periodo+self.ora_con_min_decimali(0.01):
            orario_valido=self.ora_con_min(orario_al_periodo)
            return orario_valido
        else :
            orario_valido=self.ora_con_min(orario_al_periodo+self.periodo)
            return orario_valido

    def uscita_valida(self,orario):
        orario_decimale=self.ora_con_min_decimali(orario)
        orario_al_periodo=self.approssimazione_al_periodo(orario_decimale)+self.periodo
    
        if orario_decimale < orario_al_periodo-self.ora_con_min_decimali(0.01):
            orario_valido=self.ora_con_min(orario_al_periodo-self.periodo)
            return orario_valido
        else :
            orario_valido=self.ora_con_min(orario_al_periodo)
            return orario_valido
    

