# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('cartellino', pkey='id', name_long='Cartellino', name_plural='Cartellini',caption_field='protocollo')
        self.sysFields(tbl)
        tbl.column('persona_id', size='22', name_long='Persona'
                    ).relation('persona.id',
                                relation_name='cartellino',
                                mode='foreignkey',
                                onDelete='raise')
        tbl.column('anno', dtype='year', name_long='Anno',validate_max=9999)
        tbl.column('mese_codice', dtype='L', name_long='Mese'
                    ).relation('mese.codice',
                                relation_name='cartellino',
                                mode='foreignkey',
                                onDelete='raise')

        tbl.aliasColumn('persona_nominativo','@persona_id.nominativo')
        tbl.aliasColumn('mese_codice_descrizione','@mese_codice.descrizione')
        tbl.formulaColumn('protocollo',"$persona_nominativo || ' / ' || $anno || ' / ' || $mese_codice_descrizione", name_long='Protocollo')
    
    def defaultValues(self):
        data=self.db.workdate
        anno=data.year
        return dict(anno = anno)

    def trigger_onInserted(self, record=None):
        mese=record['mese_codice']
        cartellino_id=record['id']
        anno=record['anno']
        self.db.table('ste.movimenti_cartellino').creaGiorniCartellino(cartellino_id,anno,mese)
    
    def trigger_onDeleted(self, record=None):
        cartellino_id=record['id']
        self.db.table('ste.movimenti_cartellino').eliminaGiorniCartellino(cartellino_id)