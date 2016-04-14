# -*- coding: utf-8 -*-
{
    'name': "Odoo Chile DTE's, Configuración SII",

    'summary': """
        Agrega campos para configuración de situación ante el SII, para la 
        emisión de DTE's""",

    'description': """
        Éste módulo agrega los campos y vistas necesarias para cofigurar algunos
        parámetros necesarios para la emisión de documentos tributarios electrónicos,
        de acuerdo con la información del SII por compañía.
    """,

    'author': "Faros Inversiones Ltda.",
    'website': "http://www.farosinv.cl",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}