from odoo import _, api, fields, models


class ProductAdd(models.Model):
    _inherit = 'product.template'
    
    status_kn = fields.Selection([('A','A'),('B','B')], default='A')
    cod_prov_kn = fields.Char(string="Codigo Proveedor", size = 2)
    cod_prod_kn = fields.Char(string="Codigo Producto", size= 15)
    product_name_kn = fields.Char(string="Nombre Alterno Producto", size=18)
    presentacion_kn  = fields.Char(string="Presentacion" ,size=43 )
    precio_farmacia_kn = fields.Integer(string ="Precio Farmacia", size=10)
    
    