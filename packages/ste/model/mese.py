# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('mese',pkey='codice' ,name_long='Mese', name_plural='Mesi',caption_field='descrizione', lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice', dtype='L', name_long='Mese',validate_notnull=True)
        tbl.column('descrizione', size=':10', name_long='Descrizione')
        tbl.column('nuovo_ordine', dtype='L', name_long='Nuovo Ordine', name_short='')
        