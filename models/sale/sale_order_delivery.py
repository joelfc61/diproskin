# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class SaleOrderDelivery(models.Model):
    _name = "sale.order.delivery"
    _description = "Users delivery"

    active = fields.Boolean("Active", default=True)
    user_delivery_photo = fields.Binary(string="Entrega", help='Foto')
    name = fields.Char("Entrega")