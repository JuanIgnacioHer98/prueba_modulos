# -*- coding: utf-8 -*-
from odoo import models, fields

class impreso(models.Model):
     _inherit = 'account.move'

     prueba = fields.Char(string="Prueba")


