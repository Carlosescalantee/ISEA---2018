# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class matriculas(models.Model):
#     _name = 'matriculas.matriculas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Alumno(models.Model):
    _name = 'matriculas.alumno'

    name = fields.Char(string="Nombres")
    apellidos = fields.Char(string="Apellidos")
    edad = fields.Integer(string="Edad")
    telefono = fields.Integer(string="Telefono")
    correo = fields.Char(String="Correo Electronico")
    matriculas_ids = fields.One2many(
        'matriculas.matricula', 'alumno_id', string="Matriculas")


class Curso(models.Model):
    _name = 'matriculas.curso'

    name = fields.Char(string="Nombre")
    profesor = fields.Char(string="Profesor")
    informacion = fields.Text(string="Informacion del Curso")
    horas = fields.Integer(string="Horas del Curso")
    area_ids = fields.Many2many('matriculas.area')


class Matricula(models.Model):
    _name = 'matriculas.matricula'

    name = fields.Char()
    fecha_matricula = fields.Date(string="Fecha de la Matricula")
    curso_id = fields.Many2one('matriculas.curso', string="Curso")
    alumno_id = fields.Many2one('matriculas.alumno', string="Alumno")


class Area(models.Model):
    _name = "matriculas.area"

    name = fields.Char(String="Nombre del Area")
    informacion = fields.Text(string="Informacion del Curso")
    jefe_area = fields.Text(string="Jefe del Area")
    curso_ids = fields.Many2many('matriculas.curso')
