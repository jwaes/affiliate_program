from odoo import models, fields

class SaleReport(models.Model):
    _inherit = 'sale.report'

    affiliate_id = fields.Many2one('affiliate.affiliate', string="Affiliate", readonly=True)
    program_id = fields.Many2one('affiliate.program', string="Affiliate Program", readonly=True)

    def _select(self):
        select_str = super(SaleReport, self)._select()
        select_str += """
            , s.affiliate_id as affiliate_id
            , s.program_id as program_id
        """
        return select_str

    def _group_by(self):
        group_by_str = super(SaleReport, self)._group_by()
        group_by_str += ", s.affiliate_id, s.program_id"
        return group_by_str
