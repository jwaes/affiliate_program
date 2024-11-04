from odoo.tests.common import TransactionCase

class TestSaleOrderAttribution(TransactionCase):

    def setUp(self):
        super(TestSaleOrderAttribution, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})
        self.program = self.env['affiliate.program'].create({'name': 'Test Program'})
        self.affiliate = self.partner.enroll_in_affiliate_program(self.program.id)
        self.env['ir.http'].session['affiliate_code'] = self.affiliate.unique_code  # Set session utm_source

    def test_affiliate_attribution_on_sale_order(self):
        order = self.env['sale.order'].create({'partner_id': self.partner.id})
        self.assertEqual(order.affiliate_id, self.affiliate)

    def test_invalid_utm_source_on_sale_order(self):
        self.env['ir.http'].session['affiliate_code'] = "invalid_code"
        order = self.env['sale.order'].create({'partner_id': self.partner.id})
        self.assertFalse(order.affiliate_id, "No affiliate should be assigned with an invalid UTM source")
