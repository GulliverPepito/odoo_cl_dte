# -*- coding: utf-8 -*-
from openerp import http

# class L10nClDtePaperformat(http.Controller):
#     @http.route('/l10n_cl_dte_paperformat/l10n_cl_dte_paperformat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_dte_paperformat/l10n_cl_dte_paperformat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_dte_paperformat.listing', {
#             'root': '/l10n_cl_dte_paperformat/l10n_cl_dte_paperformat',
#             'objects': http.request.env['l10n_cl_dte_paperformat.l10n_cl_dte_paperformat'].search([]),
#         })

#     @http.route('/l10n_cl_dte_paperformat/l10n_cl_dte_paperformat/objects/<model("l10n_cl_dte_paperformat.l10n_cl_dte_paperformat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_dte_paperformat.object', {
#             'object': obj
#         })