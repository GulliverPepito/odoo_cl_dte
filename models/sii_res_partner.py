# -*- coding: utf-8 -*-
# Copyright 2017 Faros Inversiones Ltda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SiiRes_partner(models.Model):

#    _name = 'sii.res_partner'
    _description = 'Partner DTE information'
    _inherit = 'res.partner'

    dte_receptor = fields.Boolean(string = 'Receptor DTE?', help = 'Partner es receptor DTE?')

    dte_partner_email = fields.Char(
                                    string = 'Email receptor DTE',
                                    store = True,
                                    size = 30,
                                    help = 'Correo electrónico para recepción de DTE')
