{
    'name': 'Customer Contracts',
    'version': '1.0',
    'category': 'Sales',
    'author': 'witdata',
    'depends': ['base', 'contacts'],
    'data': [
        'views/customer_contract_view.xml',
        'views/customer_contract_menu.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'installable': True,
    'application': True,
}
