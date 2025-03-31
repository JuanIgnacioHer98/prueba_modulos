# -*- coding: utf-8 -*-
# from odoo import http


# class Libro(http.Controller):
#     @http.route('/libro/libro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libro/libro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libro.listing', {
#             'root': '/libro/libro',
#             'objects': http.request.env['libro.libro'].search([]),
#         })

#     @http.route('/libro/libro/objects/<model("libro.libro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libro.object', {
#             'object': obj
#         })

