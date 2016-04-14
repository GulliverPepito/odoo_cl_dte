# -*- coding: utf-8 -*-

from openerp import models, fields, api

class company_sii_data(models.Model):
    _description = 'Company SII configuration'
    _inherit = 'res.company'
    
    razon_social_dte = fields.Char(
                                   string = 'Razón Social SII',
                                   store = True,
                                   help = 'Ingresar Razón Social de la empresa')
    