# -*- coding: utf-8 -*-
{
    'name': "custom invoice",

    'summary': """
        Modulo que modifica la factura""",

    'description': """
        Modulo de reportes personalizados
    """,

    'author': "Jhonny Martínez Espinoza",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}