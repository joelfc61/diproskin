from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pick_id = fields.Many2one('hr.employee', tracking=True, string='Surtido', store=True)
    delivery_id = fields.Many2one('hr.employee', tracking=True, string='Entrega', store=True)
    agent_id = fields.Many2one('hr.employee', tracking=True, string='Marcado', store=True)

    def action_print_so(self):
        return self.env.ref('diproskin.action_report_sale_remision').report_action(self)
