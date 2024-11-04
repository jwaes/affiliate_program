from odoo import models, fields, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

    affiliate_ids = fields.One2many('affiliate.affiliate', 'partner_id', string="Affiliate Programs")

    def enroll_in_affiliate_program(self, program_id):
        """Enroll the partner in the specified affiliate program if not already enrolled."""
        # Check if already enrolled
        existing_enrollment = self.env['affiliate.affiliate'].search([
            ('partner_id', '=', self.id),
            ('program_id', '=', program_id)
        ], limit=1)

        if existing_enrollment:
            raise exceptions.UserError("You are already enrolled in this affiliate program.")

        # If not already enrolled, create the affiliate record
        program = self.env['affiliate.program'].browse(program_id)
        return program.enroll_partner(self.id)
