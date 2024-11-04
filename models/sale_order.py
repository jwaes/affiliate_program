import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)  # Set up the logger

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    affiliate_id = fields.Many2one('affiliate.affiliate', string="Affiliate", help="The affiliate responsible for this sale.")
    program_id = fields.Many2one('affiliate.program', string="Affiliate Program", related="affiliate_id.program_id", store=True)

    @api.model
    def create(self, vals):
        # Check if there's an affiliate UTM source in the session
        session_affiliate_code = self.env['ir.http'].session_get('utm_source')
        
        if session_affiliate_code:
            # Try to find the affiliate based on the session UTM source code
            affiliate = self.env['affiliate.affiliate'].sudo().search([('unique_code', '=', session_affiliate_code)], limit=1)
            
            if affiliate:
                vals['affiliate_id'] = affiliate.id
            else:
                # Log a warning if the UTM source code is invalid or not found
                _logger.warning(f"Sale Order Creation: UTM source '{session_affiliate_code}' did not match any affiliate.")
                
        return super(SaleOrder, self).create(vals)
