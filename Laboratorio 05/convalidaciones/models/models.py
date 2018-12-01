# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class convalidaciones(models.Model):
#     _name = 'convalidaciones.convalidaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Alumno(models.Model):
    _name = 'convalidaciones.alumno'

    name = fields.Char(string="Nombre y Apellidos")
    edad = fields.Integer(string="Edad")


class Modulo(models.Model):
    _name = 'convalidaciones.modulo'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")