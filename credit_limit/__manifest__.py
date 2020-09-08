# -*- coding: utf-8 -*-
{
    'name': "Credit Limit",

    'summary': """Customer credit limit""",

    'description': """
Customer credit limit
=====================
* We add to partner the boolean "use credit limit". If the boolean is = true we can fill out integer field with the monetary value of the credit limit
* When creating a sales.order we need to check all open amounts from invoices for the partner
* When credit limit is exceeded
* We get a warning when "saving" a sales order - but we can save it.
* We have a read-only boolean "Credit Limit Block" on the sales.order which is set to true.
* We cannot set the sales.order to state "sale". When clicking the button we get a warning.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application': True,
    'sequence': 1, 
}