from odoo import http
from odoo.http import request

class AffiliatePortalController(http.Controller):

    @http.route('/my/affiliate_links', type='http', auth="user", website=True)
    def my_affiliate_links(self, **kwargs):
        partner = request.env.user.partner_id
        affiliate = partner.affiliate_ids[:1]  # Assuming one affiliate per partner
        if not affiliate:
            return request.redirect('/my/home')  # Redirect if no affiliate

        # Render the portal template with the affiliate's links
        return request.render('affiliate_program.portal_affiliate_links_template', {
            'affiliate': affiliate,
        })
