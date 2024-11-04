from odoo import http
from odoo.http import request
from odoo.exceptions import UserError

class AffiliateProgramController(http.Controller):

    @http.route('/affiliate/create_link', type='http', auth="user", website=True)
    def create_link_form(self, **kwargs):
        affiliate = request.env.user.partner_id.affiliate_ids[:1]  # Assuming a single affiliate per partner
        if not affiliate:
            raise UserError("You must be enrolled in an affiliate program to create links.")
        
        return request.render('affiliate_program.create_link_template', {
            'affiliate': affiliate,
        })

    @http.route('/affiliate/create_link/submit', type='http', auth="user", methods=['POST'], website=True)
    def create_link_submit(self, **post):
        target_url = post.get('target_url')
        campaign_name = post.get('campaign_name')
        affiliate = request.env.user.partner_id.affiliate_ids[:1]

        if not affiliate:
            raise UserError("You are not enrolled in an affiliate program.")

        # Create the custom tracked link
        link_tracker = affiliate.create_tracked_link(target_url, campaign_name)
        
        return request.redirect('/affiliate/links')
