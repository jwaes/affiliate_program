{
    'name': "Affiliate Program",
    'version': '17.0.1.21.0',
    'category': 'Sales/CRM',
    'summary': 'Implement an affiliate program with UTM tracking.',
    'author': 'Cline',
    'depends': ['base', 'utm', 'website_sale', 'link_tracker', 'portal', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'security/affiliate_security.xml',
        'views/affiliate_views.xml',
        'views/affiliate_templates.xml',
        'views/affiliate_portal_menu.xml',
        'views/affiliate_portal_templates.xml',
        'views/affiliate_program_views.xml',
        'views/res_partner_views.xml',
        'views/sale_report_views.xml',
        'views/sale_report_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'test': [
        'tests/test_affiliate_enrollment.py',
        'tests/test_unique_code_generation.py',
        'tests/test_link_creation.py',
        'tests/test_sale_order_attribution.py',
    ],
}
