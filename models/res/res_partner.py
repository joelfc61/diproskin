from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    comm_name = fields.Char(string='Nombre Comercial')
    