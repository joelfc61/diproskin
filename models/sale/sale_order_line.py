
from odoo import models, api, fields, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pricelist_id = fields.Many2one('product.pricelist', string='Lista de precios')

    @api.onchange('pricelist_id')
    def onchange_product_pricelist_id(self):
        if self.pricelist_id:
            product = self.product_id
            qty = self.product_uom_qty
            uom = self.product_id.uom_id
            date = self.create_date
            price_unit = self.pricelist_id._get_product_price(product, qty, uom=uom, date=date)
            self.price_unit = price_unit


    @api.depends('product_id', 'product_uom', 'product_uom_qty')
    def _compute_pricelist_item_id(self):
        for line in self:
            if not line.product_id or line.display_type or not line.order_id.pricelist_id:
                line.pricelist_item_id = False
            else:
                if line.pricelist_id:
                    line.pricelist_item_id = line.pricelist_id._get_product_rule(
                        line.product_id,
                        line.product_uom_qty or 1.0,
                        uom=line.product_uom,
                        date=line.order_id.date_order)
                else:
                    line.pricelist_item_id = line.order_id.pricelist_id._get_product_rule(
                        line.product_id,
                        line.product_uom_qty or 1.0,
                        uom=line.product_uom,
                        date=line.order_id.date_order)

    barcode_scan = fields.Char(string='Código')

    @api.onchange('barcode_scan')
    def _onchange_barcode_scan(self):
        product_rec = self.env['product.product']
        if self.barcode_scan:
            product = product_rec.search(['|',('barcode_ids.name', '=', self.barcode_scan), ('barcode', '=', self.barcode_scan)],limit=1)
            # TODO REPLACE BY multi_barcode
            # product = product_rec.search([('barcode', '=', self.barcode_scan)])
            self.product_id = product.id
