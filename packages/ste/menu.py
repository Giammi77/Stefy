#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    cartellini = root.branch(u"Gestione Cartellini")
    cartellini.thpage(u"!!Cartellino", table="ste.cartellino")
    cartellini.thpage(u"!!Persona", table="ste.persona")
    cartellini.thpage("Dati Cartellino",table='ste.movimenti_cartellino')
    cartellini.lookups('Lookup tables',lookup_manager='ste')
