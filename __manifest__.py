# -*- coding: utf-8 -*-
{
    'name': "Report Pos Cash Closing",
    'category': 'Accounting/Sale',
    'website': "",
    'version': '17.0',
    'depends': ['point_of_sale', 'l10n_latam_invoice_document'],
    'data': [

        'reports/report_saledetails.xml',
        # 'views/company_views.xml',
        'views/inherit_views.xml',

    ],
    'license': "OPL-1",
    'installable': True,
    'application': False,
}


