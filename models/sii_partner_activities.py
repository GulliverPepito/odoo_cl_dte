# -*- coding: utf-8 -*-
# Copyright 2017 Faros Inversiones Ltda.
# Based on works by @dansanti and @KonosCL on github
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

class invoice_turn(models.Model):
    _inherit = "account.invoice"

    def set_partner_activity(self):
        for default_activity in self.partner_id.partner_activities_ids:
            return default_activity

    invoice_turn = fields.Many2one(
        'partner.activities',
        'Giro',
        readonly=True,
        default=set_partner_activity,
        store=True,
        states={'draft': [('readonly', False)]})
    activity_description = fields.Many2one(
        'sii.activity.description',
        string="Giro",
        related="partner_id.activity_description",
        readonly=True)

    @api.onchange('partner_id')
    def _set_default_activity(self):
        self.invoice_turn = self.set_partner_activity()


#------------------------------------
# PARTNER ACTIVITIES
#------------------------------------


class PartnerActivities(models.Model):
    _description = 'SII Economical Activities'
    _name = 'partner.activities'

    code = fields.Char('Activity Code', required=True, translate=True)
    parent_id = fields.Many2one(
        'partner.activities', 'Parent Activity', select=True,
        ondelete='cascade')
    name = fields.Char('Nombre Completo', required=True, translate=True)
    vat_affected = fields.Selection(
        [('SI', 'Si'), ('NO', 'No'), ('ND', 'ND')], 'VAT Affected',
        required=True, translate=True, default='SI')
    tax_category = fields.Selection(
        [('1', '1'), ('2', '2'), ('ND', 'ND')], 'TAX Category', required=True,
        translate=True, default='1')
    internet_available = fields.Boolean('Available at Internet', default=True)
    active = fields.Boolean(
        'Active', help="Allows you to hide the activity without removing it.",
        default=True)
    partner_ids = fields.Many2many(
        'res.partner', id1='activities_id', id2='partner_id',
        string='Partners')


class PartnerTurns(models.Model):
    _description = 'Partner registered turns'
    _inherit = 'res.partner'

    partner_activities_ids = fields.Many2many(
        'partner.activities', id1='partner_id', id2='activities_id',
        string='Activities Names',
        help=u'Seleccione las actividades económicas registradas en el SII')


class CompanyTurns(models.Model):
    _description = 'Company registered turns'
    _inherit = 'res.company'

    company_activities_ids = fields.Many2many(
        string='Activities Names',
        related='partner_id.partner_activities_ids',
        relation='partner.activities',
        help=u'Seleccione las actividades económicas registradas en el SII')



#------------------------------------
# ACTIVITIES DESCRIPTION
#------------------------------------

class PartnerActivities(models.Model):
    _description = 'SII Economical Activities Printable Description'
    _name = 'sii.activity.description'

    name = fields.Char('Glosa', required=True, translate=True)
    vat_affected = fields.Selection(
        [('SI', 'Si'), ('NO', 'No'), ('ND', 'ND')], 'VAT Affected',
        required=True, translate=True, default='SI')
    active = fields.Boolean(
        'Active', help="Allows you to hide the activity without removing it.",
        default=True)

class PartnerTurns(models.Model):
    _inherit = 'res.partner'
    activity_description = fields.Many2one(
        'sii.activity.description',
        string='Glosa Giro', ondelete="restrict")

class CompanyTurns(models.Model):
    _inherit = 'res.company'
    activity_description = fields.Many2one(
        string='Glosa Giro',
        related='partner_id.activity_description',
        relation='sii.activity.description')
