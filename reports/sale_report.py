
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"


    line_pricelist_id = fields.Many2one('product.pricelist', string='Lista de precios Linea')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['line_pricelist_id'] = "l.pricelist_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            l.pricelist_id"""
        return res
