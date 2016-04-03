# -*- coding: utf-8 -*-
from openerp import http

# class L10nClDte(http.Controller):
#     @http.route('/l10n_cl_dte/l10n_cl_dte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_dte/l10n_cl_dte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_dte.listing', {
#             'root': '/l10n_cl_dte/l10n_cl_dte',
#             'objects': http.request.env['l10n_cl_dte.l10n_cl_dte'].search([]),
#         })

#     @http.route('/l10n_cl_dte/l10n_cl_dte/objects/<model("l10n_cl_dte.l10n_cl_dte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_dte.object', {
#             'object': obj
#         })