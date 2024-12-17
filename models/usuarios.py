"""usuarios"""


from odoo import models, fields

class Hermanos(models.Model):
    """Clase Hermanos"""
    _name = 'usuarios.libros'
    _description = "Modelo de Usuarios que podrán adquirir libros"
    _rec_name = 'nombre_hermano'

    nombre_hermano = fields.Char(string="Hermano(a)")
    celular = fields.Integer(string="Celular")
    direccion = fields.Char(string="Dirección")
