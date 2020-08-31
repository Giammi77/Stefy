#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound
from gnr.core.gnrbag import Bag
from gnrpkg.ste.approssimazione import tempo_lavoro

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cartellino_id')
        r.fieldcell('data')
        r.fieldcell('prima_entrata')
        r.fieldcell('prima_uscita')
        r.fieldcell('seconda_entrata')
        r.fieldcell('seconda_uscita')
        r.fieldcell('terza_entrata')
        r.fieldcell('terza_uscita')
        r.fieldcell('ore_ordinarie')
        r.fieldcell('ore_straordinarie')
        r.fieldcell('totale_ore')
    def th_order(self):
        return 'cartellino_id'

    def th_query(self):
        return dict(column='cartellino_id', op='contains', val='')

class ViewFromCartellino(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data',edit=False,
                    giorno_settimanale='1',
                    color='^dow?red: green'
                    )
        r.fieldcell('dow')
        r.fieldcell('prima_entrata',edit=dict(remoteRowController=True))
        r.fieldcell('prima_uscita',edit=dict(remoteRowController=True))
        r.fieldcell('seconda_entrata',edit=dict(remoteRowController=True))
        r.fieldcell('seconda_uscita',edit=dict(remoteRowController=True))
        r.fieldcell('terza_entrata',edit=dict(remoteRowController=True))
        r.fieldcell('terza_uscita',edit=dict(remoteRowController=True))
        r.fieldcell('ore_ordinarie')
        r.fieldcell('ore_straordinarie')
        r.fieldcell('totale_ore')

    def th_hiddencolumns(self):
        return '$dow_number'

    @public_method
    def th_remoteRowController(self,row=None,field=None,**kwargs):
        row_attr=kwargs['row_attr']
        giorno_settimanale=row_attr['dow_number']
        if giorno_settimanale == 6 :
            ordinarie=4
        elif giorno_settimanale == 0 :
            ordinarie=0
        else :
            ordinarie=8
        lista_campi=['prima_entrata','prima_uscita','seconda_entrata','seconda_uscita','terza_entrata','terza_uscita']
        for e in lista_campi:
            if not row[e]:
                row[e]=0
        
        prima= tempo_lavoro()
        seconda=tempo_lavoro()
        terza=tempo_lavoro()

        prima.entrata=row['prima_entrata']
        prima.uscita=row['prima_uscita']

        seconda.entrata=row['seconda_entrata']
        seconda.uscita=row['seconda_uscita']

        terza.entrata=row['terza_entrata']
        terza.uscita=row['terza_uscita']
        totale_ore=prima.lavorato()+seconda.lavorato()+terza.lavorato()

        if totale_ore>ordinarie:
            row['ore_ordinarie']=ordinarie
            row['ore_straordinarie']=totale_ore-ordinarie
        else:
            row['ore_ordinarie']=totale_ore
        row['totale']


        return row




        # field = field or 'prodotto_id' #nel caso di inserimento batch il prodotto viene considerato campo primario
        # if not row['prodotto_id']:
        #     return row
        # if not row['quantita']:
        #     row['quantita'] = 1
        # if field == 'prodotto_id':
        #     prezzo_unitario,aliquota_iva = self.db.table('fatt.prodotto').readColumns(columns='$prezzo_unitario,@tipo_iva_codice.aliquota',pkey=row['prodotto_id'])
        #     row['prezzo_unitario'] = prezzo_unitario
        #     row['aliquota_iva'] = aliquota_iva
        # row['prezzo_totale'] = decimalRound(row['quantita'] * row['prezzo_unitario'])
        # row['iva'] = decimalRound(old_div(row['aliquota_iva'] * row['prezzo_totale'],100))
        return row

    def th_order(self):
        return 'data'

    def th_query(self):
        return dict(column='cartellino_id', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        center=bc.contentPane(region='center',datapath='.record')
        fb = center.formbuilder(cols=2, border_spacing='4px')
        fb.field('cartellino_id')
        fb.field('data')
        fb.field('prima_entrata')
        fb.field('prima_uscita')
        fb.field('seconda_entrata')
        fb.field('seconda_uscita')
        fb.field('terza_entrata')
        fb.field('terza_uscita')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

