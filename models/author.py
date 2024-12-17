from odoo import models, fields

class Autor(models.Model):
    """Clase Autor"""
    _name = 'autor'
    _description = 'Informacion del autor del libro'
    _rec_name = 'name'
    
    name = fields.Char(string="Nombre del Autor: ", required=True)
    last_name = fields.Char(string="Apellido del Autor")
    fecha_nacimiento = fields.Date(string="Año de Nacimiento")
