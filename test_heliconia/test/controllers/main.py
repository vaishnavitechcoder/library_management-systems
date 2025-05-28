from odoo import http
from odoo.http import request, route
import random
import json
from datetime import datetime
from odoo import http
from odoo.http import request
from odoo.osv import expression
from odoo.addons.portal.controllers.portal import CustomerPortal

class Test(http.Controller):

    # @http.route('/website/sale/new/page', auth='user', type='http')
    # def new_page(self, **kwargs):
    #     product = request.env['product.template'].search([])
    #     return request.render('librarys.new_sale_website', {'products': product})
    #
    # @http.route('/new/submit', type='http', auth='user', website=True, csrf=True)
    # def submit_borrow_form(self, **post):
    #     member = request.env['res.partner'].sudo().search([], limit=1)
    #     if not member:
    #         return request.redirect('/library/borrow')
    #
    #     request.env['crm.lead'].sudo().create({
    #         'partner_id': member.id,
    #         'product_id': int(post.get('product_id')) if post.get('product_id') else False,
    #         'quantity': int(post.get('quantity')) if post.get('quantity') else False,
    #     })
    #     return request.redirect('/library/borrow/thankyou')

    # @route(['/new/<model("product.template"):product>'], type='http', auth="public", website=True,
    #        sitemap=sitemap_products, readonly=True)
    # def product(self, product, category='', search='', **kwargs):
    #     if not request.website.has_ecommerce_access():
    #         return request.redirect('/web/login')
    #
    #     return request.render("website_sale.product", self._prepare_product_values(product, category, search, **kwargs))

    @http.route('/get-best-price', type='http', auth='public', website=True)
    def get_best_price(self, product_id=None):
        product = request.env['product.template'].sudo().browse(product_id)
        return request.render('librarys.get_best_price_page', {
            'product': product,
            'name': product.name
        })

    @http.route('/submit-best-price', type='http', auth='public', website=True, csrf=True)
    def submit_best_price(self, **post):
        product_name = post.get('product_name')
        quantity = post.get('quantity')
        timeline = post.get('timeline')
        email = post.get('email')
        request.env['crm.lead'].sudo().create({
            'name': f"Best Price Request for {product_name}",
            'contact_name': email,
            'email_from': email,
            'description': f"Quantity: {quantity}\nTimeline: {timeline}"
        })

        return request.render('librarys.best_price_thank_you')

    @http.route('/best-price-success', type='http', auth='public', website=True)
    def best_price_success(self):
        return request.render('website_sale.best_price_thank_you')
