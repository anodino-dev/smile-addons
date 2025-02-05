# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    'name': "Smile Event Refund Registration",

    'description': """
          Cancel and Refund event
    """,
    'author': "Smile",
    "license": 'LGPL-3',
    'website': "http://www.smile.eu",
    'category': 'tools',
    'version': '14.0.1.0.0',

    'depends': [
        'base',
        'website_event',
        'event_sale',
    ],

    'data': [
        'data/email_template.xml',
        'security/ir.model.access.csv',
        'wizard/event_refund_view.xml',
        'views/event_registration.xml',
    ],
}
