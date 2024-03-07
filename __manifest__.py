# -*- coding: utf-8 -*-
{
    'name': "Sally Flower Shop",

    'summary': "flower shop for btco",

    'description': "Flower shop module for Sally",

    'author': "Fayiz Asad",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock','sale_stock','website_sale'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'reports/sales_order_report.xml',
        'data/ir_action_data.xml',
        'data/scheduled_action.xml',
        'data/config_parameter.xml',
        'data/order_paperformat.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/flower_shop_view.xml',
        'views/flower_shop_menu.xml',
        'views/flower_shop_product_template_view.xml',
        'views/flower_shop_product_menu_view.xml',
        'views/flower_shop_sale_order_line_view.xml',
        'views/flower_shop_stock_lot_view.xml',
        'views/flower_shop_watering_times.xml',
        'views/flower_shop_water_menu.xml',
        'views/stock_warehouse_weather_view.xml',
        'views/flower_shop_web_sale_view.xml',
        'views/flower_shop_sale_report_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
