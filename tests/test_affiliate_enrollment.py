from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestAffiliateEnrollment(TransactionCase):

    def setUp(self):
        super(TestAffiliateEnrollment, self).setUp()
        self.program = self.env['affiliate.program'].create({'name': 'Test Program'})
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})

    def test_enrollment(self):
        """Test enrolling a partner."""
        self.partner.enroll_in_affiliate_program(self.program.id)
        affiliate = self.env['affiliate.affiliate'].search([
            ('partner_id', '=', self.partner.id),
            ('program_id', '=', self.program.id)
        ])
        self.assertTrue(affiliate, "Affiliate record not created.")
        self.assertTrue(affiliate.unique_code, "Unique code not generated.")

    def test_duplicate_enrollment_prevention(self):
        """Test preventing duplicate enrollment."""
        self.partner.enroll_in_affiliate_program(self.program.id)
        with self.assertRaises(UserError):
            self.partner.enroll_in_affiliate_program(self.program.id)
