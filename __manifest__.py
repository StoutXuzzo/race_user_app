# -*- coding: utf-8 -*-
{
    'name': "race_user_app",

    'summary': """
        race_app with ineritance
        """,

    'description': """
        race_app with ineritance but long
    """,

    'author': "JosepPla",
    'website': "https://www.youtube.com/watch?v=ZGH3Y0pqzkY",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['race_app'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pilot_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
     'installable': True,
}
