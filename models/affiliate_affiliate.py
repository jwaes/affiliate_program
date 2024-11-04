import hashlib
import random
from odoo import models, fields, api

class Affiliate(models.Model):
    _name = 'affiliate.affiliate'
    _description = 'Affiliate'


    partner_id = fields.Many2one('res.partner', string="Affiliate Partner", required=True)
    partner_name = fields.Char(string="Name", related="partner_id.name", readonly=True, store=True)
    program_id = fields.Many2one('affiliate.program', string="Affiliate Program", required=True)
    utm_source_id = fields.Many2one('utm.source', string="UTM Source", readonly=True) # Added back
    unique_code = fields.Char(string="Unique Code", readonly=True, index=True, unique=True)

    link_tracker_ids = fields.One2many('link.tracker', 'affiliate_id', string="Tracked Links")

    _sql_constraints = [
        ('unique_partner_program', 'unique(partner_id, program_id)', 
         'Each partner can only enroll once in each affiliate program.')
    ]

    @api.model
    def create(self, vals):
        affiliate = super(Affiliate, self).create(vals)
        affiliate._generate_unique_code() # Ensure unique code is generated on creation
        # Create a UTM source
        source_name = f"AFF_{affiliate.unique_code}"
        utm_source = self.env['utm.source'].create({'name': source_name})
        affiliate.utm_source_id = utm_source.id # Associate UTM source with affiliate
        return affiliate

    def _generate_unique_code(self):
        """Generate a unique code for the affiliate with collision handling."""
        while True:
            # Generate a hash from a unique string based on ID and a random component for added uniqueness
            unique_string = f"{self.id}_{self.program_id.id}_{random.randint(0, 9999)}"
            hash_object = hashlib.sha1(unique_string.encode())
            code_numeric = int(hash_object.hexdigest(), 16) % (36**6)
            new_code = base36encode(code_numeric).upper()
            
            # Check for collisions
            if not self.search([('unique_code', '=', new_code)], limit=1):
                self.unique_code = new_code
                break  # Exit the loop if the code is unique



    def create_tracked_link(self, target_url, campaign=None):
        """Creates a new tracked link for the affiliate."""
        campaign_name = campaign or self.program_id.name
        return self.env['link.tracker'].create({
            'name': f"{self.partner_id.name} - {campaign_name}",
            'url': target_url,
            'utm_source_id': self.utm_source_id.id,
            'utm_medium': 'affiliate',
            'utm_campaign': campaign_name,
            'affiliate_id': self.id,
        })            

# Helper function for Base36 encoding
def base36encode(number):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while number > 0:
        number, i = divmod(number, 36)
        result = chars[i] + result
    return result or '0'
