# -*- coding: utf-8 -*-

from odoo import models, fields


class Estudiante(models.Model):
    _name = 'estudiantes.estudiante'
    _description = 'estudiantes.estudiante'

    name = fields.Char(string="Nombre",required=True)
    age = fields.Integer(string="Edad")
    year = fields.Char(string="Año")
    email = fields.Char(string="Email")
    materia_ids = fields.Many2many(
        'estudiantes.materia',
        'estudiantes_estudiante_materia_rel',
        'estudiante_id',
        'materia_id',
        string='Materias'
    )


