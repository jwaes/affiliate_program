from odoo.tests.common import TransactionCase

class TestUniqueCodeGeneration(TransactionCase):

    def setUp(self):
        super(TestUniqueCodeGeneration, self).setUp()
        self.program = self.env['affiliate.program'].create({'name': 'Test Program'})

    def test_unique_code_generation(self):
        partner1 = self.env['res.partner'].create({'name': 'Partner 1'})
        partner2 = self.env['res.partner'].create({'name': 'Partner 2'})
        affiliate1 = partner1.enroll_in_affiliate_program(self.program.id)
        affiliate2 = partner2.enroll_in_affiliate_program(self.program.id)

        self.assertNotEqual(affiliate1.unique_code, affiliate2.unique_code)
