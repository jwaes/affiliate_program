from odoo.tests.common import TransactionCase

class TestLinkCreation(TransactionCase):

    def setUp(self):
        super(TestLinkCreation, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})
        self.program = self.env['affiliate.program'].create({'name': 'Test Program'})
        self.affiliate = self.partner.enroll_in_affiliate_program(self.program.id)

    def test_custom_link_creation(self):
        target_url = "https://example.com/product"
        campaign_name = "Special Campaign"
        link = self.affiliate.create_tracked_link(target_url, campaign_name)
        
        self.assertEqual(link.url, target_url)
        self.assertEqual(link.utm_source_id.name, f"AFF_{self.affiliate.unique_code}")
        self.assertEqual(link.utm_campaign, campaign_name)
