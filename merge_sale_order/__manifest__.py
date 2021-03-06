# -*- coding: utf-8 -*-

{
    'name': 'Merge Sale Order',
    'category': 'Sales',
    'version': '1.1',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Merge Sale Order',

    'depends': [
        'sale_management'
    ],

    'data': [
        'wizard/merge_sale_order_wizard_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'auto_install': False,
    'installable': True,
    'application': False

}
