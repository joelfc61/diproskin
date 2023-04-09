# -*- coding: utf-8 -*-
{
    'name': "diproskin",
    'summary': """
        DiproSkin""",
    'description': """
        Customs DiproSkin
    """,
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
                'sale_management',
                'product_multiple_barcodes',
                'hr',
                ],
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_sale_remision.xml',
        'report/sale_views.xml',
        'views/sale_order_views.xml',
    ],
    'qweb': [
    ],
}
