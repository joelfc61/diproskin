# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class SaleOrderPick(models.Model):
    _name = "sale.order.pick"
    _description = "Users picking"

    active = fields.Boolean("Active", default=True)
    user_pick_photo = fields.Binary(string="Surtidor", help='Foto')
    name = fields.Char("Surtido")