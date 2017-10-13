# -*- coding: utf-8 -*-
# Copyright 2017 Faros Inversiones Ltda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountDte_type(models.Model):

    _name = 'account.dte_type'
    _description = 'Account Dte_type'

    name = fields.Char()
    sii_code = fields.Integer('sii code')
    odoo_code = fields.Char('Odoo Code')
    model_id = fields.Many2one(
        'ir.model',
        string='Model',
        help="Modelo relacionado."
    )


class Account_invoice(models.Model):

    _inherit = 'account.invoice'

    dte_type = fields.Many2one(
        'account.dte_type',
        domain="[('model_id.model', 'ilike', 'account.invoice')]",
        string='Tipo de DTE',
        required=True
    )
