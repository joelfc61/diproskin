# -*- coding: utf-8 -*-
{
    'name': "diproskin",
    'summary': """
        DiproSkin""",
    'description': """
        Customs DiproSkin
    """,
     'sequence': -100,
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'purchase',
        'sale_management',
        'product_multiple_barcodes',
        'hr','product'
    ], 
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_sale_remision.xml',
        'reports/actions_reports.xml',
        'reports/report_remision_view.xml',
        'report/sale_views.xml',
        'views/sale_order_views.xml',
        'views/customer_view.xml',
        'views/product_add_view.xml'
    ],
    'qweb': [
    ],
}
