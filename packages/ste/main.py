#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='ste package',sqlschema='ste',sqlprefix=True,
                    name_short='Ste', name_long='Ste', name_full='Ste')
                    
    def config_db(self, pkg):
        pass

    def custom_type_year(self):
        return dict(dtype='I',format='####')
        
class Table(GnrDboTable):
    pass
