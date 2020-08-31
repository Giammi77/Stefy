# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('persona', pkey='id', name_long='Persona', name_plural='Persone',caption_field='nominativo')
        self.sysFields(tbl)
        tbl.column('cognome', size=':30', name_long='Cognome',validate_case='c')
        tbl.column('nome', size=':30', name_long='Nome',validate_case='c')
        tbl.formulaColumn('nominativo',"$cognome || ' ' || $nome")