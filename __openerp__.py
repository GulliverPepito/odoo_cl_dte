# -*- coding: utf-8 -*-
{
    'name': "Odoo - Generación de Documentos Tributarios Electrónicos Chile",

    'summary': """
        Emisión de documentos tributarios electrónicos de acuerdo a la legislación Chilena.""",

    'description': """
        Módulos para la emisión de documentos tributarios electrónicos Chile.
    """,

    'author': "Faros Inversiones Ltda.",
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
        'reports/dte_cl_paperformats.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}