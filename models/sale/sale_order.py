from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pick_id = fields.Many2one('hr.employee', tracking=True, string='Surtido', store=True)
    delivery_id = fields.Many2one('hr.employee', tracking=True, string='Entrega', store=True)
    agent_id = fields.Many2one('hr.employee', tracking=True, string='Marcado', store=True)
    product_total = fields.Integer(string='Total de Productos', compute='_product_total')

    def action_print_so(self):
        return self.env.ref('diproskin.action_report_so_diproskin').report_action(self)

    @api.onchange("order_line")
    def _product_total(self):
        for order in self:
            total_quantity = sum(product.product_uom_qty for product in order.order_line)
            order.product_total = total_quantity
