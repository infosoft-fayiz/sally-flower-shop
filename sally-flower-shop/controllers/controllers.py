# -*- coding: utf-8 -*-
# from odoo import http


# class Sally-flower-shop(http.Controller):
#     @http.route('/sally-flower-shop/sally-flower-shop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sally-flower-shop/sally-flower-shop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sally-flower-shop.listing', {
#             'root': '/sally-flower-shop/sally-flower-shop',
#             'objects': http.request.env['sally-flower-shop.sally-flower-shop'].search([]),
#         })

#     @http.route('/sally-flower-shop/sally-flower-shop/objects/<model("sally-flower-shop.sally-flower-shop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sally-flower-shop.object', {
#             'object': obj
#         })
