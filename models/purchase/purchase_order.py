from odoo import api, models, fields
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    @api.model
    def create(self,vals_list):
        partner = self.env['purchase.order'].search([('partner_ref', '=', vals_list['partner_ref'])])
        if not partner:
            return super(PurchaseOrder,self).create(vals_list)
        else:
            raise UserError(("Ya Existe Una Solicitud de cotizacion con esa Referencia."))