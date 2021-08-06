# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fctgga_alumno(models.Model):
    _name = 'fctgga.alumno'
    name = fields.Char(string="Codigo", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha = fields.Date(string="Fecha de nacimiento", required=True)
    ciclo = fields.Selection([('SMR','0'),('1','DAM'),('2','DAW'),('3','ASIR')], string="Ciclo formativo")
    nota = fields.Float(string="Nota media")
    nota_texto = fields.Char(string="_notamedia", store=True)
    empresa = fields.Many2one("fctgga.empresa", string="Empresa")

    @api.onchange('nota')
    def _notamedia(self):
        for record in self:
            if record.nota>=5 and record.nota<7:
                record.nota_texto="Aprobado"
            else:
                if record.nota>=7 and record.nota<9:
                    record.nota_texto="Notable"
                else:
                    if record.nota>=9 and record.nota<=10:
                        record.nota_texto="Sobresaliente"


class fctgga_empresa(models.Model):
    _name = 'fctgga.empresa'
    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Char(string="Dirección", required=True)
    lista = fields.One2many("fctgga.alumno", "empresa", string="Lista de alumnos que han hecho la práctica en esta empresa")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
