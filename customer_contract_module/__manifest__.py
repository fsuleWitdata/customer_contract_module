{
    'name': 'Customer Contracts',
    'version': '1.0',
    'category': 'Sales',
    'author': 'witdata',
    "images":['static/description/main_screenshot.png'],
    'summary': 'Module to save contracts with clients.',
    'description': """
        App Module to save contracts with clients, hours, date range, status.
    """,
    'depends': ['base', 'contacts'],
    "license" : "	AGPL-3",
    'data': [
        'views/customer_contract_view.xml',
        'views/customer_contract_menu.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
