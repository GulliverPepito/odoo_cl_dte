# -*- coding: utf-8 -*-
{
    'name': "l10n_cl_rut",

    'summary': """
        Agrega campo RUT formateado de acuerdo a formato chileno para imprimir, sirve
        para la imprsion de RUT en facturas electrónicas""",

    'description': """
        Agrega campo RUT formateado de acuerdo a formato chileno para imprimir, sirve
        para la imprsion de RUT en facturas electrónicas
    """,

    'author': "Faros Inversiones Ltda",
    'website': "http://www.farosinv.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}