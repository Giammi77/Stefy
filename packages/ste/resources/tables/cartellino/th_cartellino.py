#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo', width='30')

    def th_order(self):
        return 'persona_id'

    def th_query(self):
        return dict(column='persona_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc= form.center.borderContainer()
        top=bc.contentPane(region='top', datapath='.record')
        center=bc.contentPane(region='center')
    
        self.datiCartellino(center)

        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('persona_id')
        fb.field('anno')
        fb.field('mese_codice',hasdownarrow=True,rowcaption='$nuovo_ordine,$descrizione')

    def datiCartellino(self,pane):
        pane.inlineTableHandler(relation='@movimenti_cartellino',
        viewResource='ViewFromCartellino',
        condition="""$cartellino_id = :id""",
        condition_id='^ste_cartellino.form.pkey',
        condition_onStart=True,
        autosave=True,
        addrow=False,
        delrow=False,
        export=True)
        # default_data='nuova_data')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
