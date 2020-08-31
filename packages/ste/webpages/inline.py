# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        root.data('miodato',9)
        bc = root.borderContainer(datapath='main') 
        center=bc.contentPane(region='center')
        bottom=bc.contentPane(region='bottom', height='300px')
        self.inline(center)
        self.thform(bottom)


    def inline(self, pane):
        pippo= "^miodato"
        pane.inlineTableHandler(table='ste.movimenti_cartellino',viewResource='ViewFromCartellino',default_prima_entrata=pippo)

    def thform(self, pane):
        pane.thFormHandler(table='ste.movimenti_cartellino',formResource='Form')
