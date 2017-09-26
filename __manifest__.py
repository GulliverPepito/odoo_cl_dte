# -*- coding: utf-8 -*-
# Copyright 2017 Faros Inversiones Ltda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Odoo Cl Dte',
    'description': """
        Documentos tributarios electrónicos con Odoo, de acuerdo a la legislación chilena.""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Faros Inversiones Ltda.',
    'website': 'www.farosinv.cl',
    'depends': [
    ],
    'data': [
        'security/sii_partner_activities.xml',
        'views/sii_partner_activities.xml',
        'data/partner.activities.csv',
    ],
    'demo': [
    ],
}
