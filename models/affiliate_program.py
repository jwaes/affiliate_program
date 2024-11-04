from odoo import models, fields, api

class AffiliateProgram(models.Model):
    _name = 'affiliate.program'
    _description = 'Affiliate Program'

    name = fields.Char(string="Program Name", required=True)
    description = fields.Text(string="Description")
    commission_rate = fields.Float(string="Commission Rate (%)", help="Default commission rate for this program.")
    active = fields.Boolean(string="Active", default=True)
    affiliate_ids = fields.One2many('affiliate.affiliate', 'program_id', string="Affiliates")

    def enroll_partner(self, partner_id):
        """Enrolls a partner into the affiliate program, creating a unique tracking code."""
        self.ensure_one()
        # Create a new affiliate and generate unique_code as needed
        affiliate = self.env['affiliate.affiliate'].create({
            'program_id': self.id,
            'partner_id': partner_id,
        })
        return affiliate
