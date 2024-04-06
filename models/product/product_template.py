from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    status_kn = fields.Selection([('A','A'),('B','B')], default='A')
    cod_prov_kn = fields.Char(string="Codigo Proveedor", size = 2)
    cod_prod_kn = fields.Char(string="Codigo Producto", size= 15)
    product_name_kn = fields.Char(string="Nombre Alterno Producto")
    presentacion_kn  = fields.Char(string="Presentacion" )
    precio_farmacia_kn = fields.Integer(string ="Precio Farmacia")
    
