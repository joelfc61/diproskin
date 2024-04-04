from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'res.partner'
    
    comm_name = fields.Char(string='Nombre Comercial', size=30)
    