# -*- coding: utf-8 -*-

from odoo import models, fields


class Materia(models.Model):
     _name = 'estudiantes.materia'
     _description = 'estudiantes.materia'

     name = fields.Char(string="Nombre",required=True)
     codigo = fields.Char(string="Codigo")


