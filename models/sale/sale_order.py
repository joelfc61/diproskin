from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pick_id = fields.Many2one('hr.employee', tracking=True, string='Surtido', store=True)
    delivery_id = fields.Many2one('hr.employee', tracking=True, string='Entrega', store=True)
    agent_id = fields.Many2one('hr.employee', tracking=True, string='Marcado', store=True)
    product_total = fields.Integer(string='TOTAL DE PRODUCTOS',compute='_product_total')

    def action_print_so(self):
        return self.env.ref('diproskin.action_report_sale_remision').report_action(self)

    def _product_total(self):
        for order in self:
            for product in order.order_line:
                order.product_total+= product.product_uom_qty