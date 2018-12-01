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
    localidad = fields.Char(string="Localidad")
    provincia = fields.Char(string="Provincia")
    email = fields.Char(string="Email")
    convalidaciones_ids = fields.One2many('convalidaciones.convalidacion','alumno_id',string="Convalidaciones del alumno")


class Modulo(models.Model):
    _name = 'convalidaciones.modulo'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    ciclo_ids = fields.Many2many('convalidaciones.ciclo')

class Convalidacion(models.Model):
    _name = 'convalidaciones.convalidacion'

    name = fields.Char()
    fecha_convalidacion = fields.Date(string="Fecha de convalidación")
    modulo_id = fields.Many2one('convalidaciones.modulo',string="Módulo")
    alumno_id = fields.Many2one('convalidaciones.alumno', string="Alumno")

class Ciclo(models.Model):
    _name = "convalidaciones.ciclo"

    name = fields.Char(String="Nombre")
    description = fields.Text(string = "Descripción")
    modulo_ids = fields.Many2many('convalidaciones.modulo')