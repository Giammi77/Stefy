# encoding: utf-8
import calendar 
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('movimenti_cartellino', pkey='id', name_long='Entrata-Uscita ', name_plural='Entrate-Uscite'
                        ,caption_field='protocollo')
        self.sysFields(tbl)
        tbl.column('cartellino_id', size=':22', name_long='Cartellino'
                ).relation('cartellino.id',
                            relation_name='movimenti_cartellino',
                            mode='foreignkey',
                            onDelete='cascade')
        tbl.column('data', dtype='D', name_long='Data')
        tbl.column('prima_entrata', dtype='N', name_long='Prima Entrata')
        tbl.column('prima_uscita', dtype='N', name_long='Prima Uscita')
        tbl.column('seconda_entrata', dtype='N', name_long='Seconda Entrata')
        tbl.column('seconda_uscita', dtype='N', name_long='seconda Uscita')
        tbl.column('terza_entrata', dtype='N', name_long='Terza Entrata')
        tbl.column('terza_uscita', dtype='N', name_long='Terza Uscita')
        tbl.column('ore_ordinarie', dtype='N', name_long='Ore ordinarie')
        tbl.column('ore_straordinarie', dtype='N', name_long='Ore straordinarie')

        tbl.aliasColumn('cartellino_protocollo','@cartellino_id.protocollo')
        tbl.formulaColumn('movimento', "$cartellino_protocollo || '/' || $data")
        tbl.formulaColumn("totale_ore","$ore_ordinarie + $ore_straordinarie", name_long='Totale ore')
        tbl.formulaColumn("dow_number","extract(dow from $data)")

        tbl.formulaColumn("dow","to_char($data,'Day')",name_long='Giorno')
      

  

    # def trigger_onInserting(self, record=None):
    #     print(x)

    def creaGiorniCartellino(self,cartellino_id,anno,mese):
        giorni_mese=calendar.monthcalendar(anno,mese)
        for settimana in giorni_mese:
            for g in settimana:
                if g!=0:
                    data=str(anno)+'-'+str(mese)+'-'+str(g)
                    nuovo_giorno = self.newrecord(cartellino_id= cartellino_id,data=data)
                    self.insert(nuovo_giorno)
        
        # id=self.pkeyValue(newPref) ne restituisce uno ma non capisco a cosa si riferisce..
        self.db.commit()
        return 
    
    def eliminaGiorniCartellino(self,cartellino_id):
        self.deleteSelection(columns='$id',
                                where='$id=:p',
                                p= cartellino_id)
        self.db.commit()