# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FacturaExenta(models.Model):
    _inherit = 'account.invoice'
    
    factura_exenta = fields.Boolean(string="Es Factura exenta?", help="Indique si es factura Exenta de IVA")
    