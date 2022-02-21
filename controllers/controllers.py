# -*- coding: utf-8 -*-
# from odoo import http


# class RaceUserApp(http.Controller):
#     @http.route('/race_user_app/race_user_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/race_user_app/race_user_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('race_user_app.listing', {
#             'root': '/race_user_app/race_user_app',
#             'objects': http.request.env['race_user_app.race_user_app'].search([]),
#         })

#     @http.route('/race_user_app/race_user_app/objects/<model("race_user_app.race_user_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('race_user_app.object', {
#             'object': obj
#         })
