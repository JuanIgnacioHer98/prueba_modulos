from odoo import models, fields

class albaran(models.Model):
     _inherit = 'stock.picking'

     x_num_albaran = fields.Char(string="Nº Albarán")