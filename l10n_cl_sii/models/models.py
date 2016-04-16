# -*- coding: utf-8 -*-

from openerp import models, fields, api

class company_sii_data(models.Model):
    _description = 'Company SII configuration'
    _inherit = 'res.company'
    
    razon_social_dte = fields.Char(
                                   string = 'Razón Social SII',
                                   store = True,
                                   size = 60,
                                   help = 'Ingresar Razón Social de la empresa')
    
    emisor_dte = fields.Boolean(string = 'Emisor DTE', help = 'Es emisor autorizado DTE?')
    
    email_dte = fields.Char(
                            string = 'Email DTE',
                            store = True,
                            size = 30,
                            help = 'Correo electrónico para recepción de DTE y respuestas del SII')
    
    legal_rep_name = fields.Char(
                                 string = 'Representante Legal',
                                 store = True,
                                 help = 'Nombre completo del Representante Legal de la empresa')
    
    sii_office = fields.Char(
                             string = 'Oficina SII',
                             store = True,
                             size = 30,
                             help = 'Oficina del SII para trámites presenciales')
    
    res_date = fields.Char(
                           string = 'Resolución SII Dte', 
                           size = 30,
                           help = 'Indicar número de resolución y año')
    
    
class partner_sii_data(models.Model):
    _description = 'Partner DTE information'
    _inherit = 'res.partner'
    
    dte_receptor = fields.Boolean(string = 'Receptor DTE?', help = 'Partner es receptor DTE?')
    
    dte_partner_email = fields.Char(
                                    string = 'Email receptor DTE',
                                    store = True,
                                    size = 30,
                                    help = 'Correo electrónico para recepción de DTE')