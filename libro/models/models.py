# -*- coding: utf-8 -*-

from odoo import models, fields #api


class Libro(models.Model):
     #uso interno
     #vemos que name tiene libro.libro que es nombre del modulo y nombre de la clase.
     _name = 'libro.libro'
     _description = 'libro.libro'

     name = fields.Char(string="Nombre")


