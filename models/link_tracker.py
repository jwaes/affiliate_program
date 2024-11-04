from odoo import models, fields

class LinkTracker(models.Model):
    _inherit = 'link.tracker'

    affiliate_id = fields.Many2one('affiliate.affiliate', string="Affiliate", help="The affiliate who owns this tracked link.")
