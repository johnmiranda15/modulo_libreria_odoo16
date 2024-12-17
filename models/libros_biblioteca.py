"""libros"""

from odoo import models, fields, api

#Creando un modelo ( tabla de datos) a partir de una clase
class Libros(models.Model):
    """Clase Libros Biblioteca"""
    _name = 'libros.biblioteca' #nombre de la tabla que se va a generar
    _description = 'Informacion de cada libro'
    _inherit = ['mail.thread','mail.activity.mixin']
                
    name = fields.Char(string = "Nombre del libro", required=True, tracking=True) #nombre del campo que es de tipo cadena
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del Autor")
    image = fields.Binary(string="Image")
    fecha_publicacion = fields.Date(string="Fecha de Publicación")
    categoria_id = fields.Many2one(comodel_name='categoria.libro')
    #campos de asignacion de libros
    hermano = fields.Many2one(comodel_name='usuarios.libros', string="Hermano(a)")
    fecha_entrega = fields.Date(string="Fecha de Entrega")
    fecha_recibido = fields.Date(string="Fecha de Recibido")
    dias_transcurridos = fields.Integer(string="Días Transcurridos", compute="_compute_dias_transcurridos")
    state = fields.Selection([
        ('available', 'Disponible'),
        ('reserved', 'Reservado'),
        ('loaned', 'Prestado'),
        ('overdue', 'Retrasado'),
        ('returned', 'Retornado'),
        ('lost', 'Perdido'),
        ('damaged', 'Dañado'),
        ('maintenance', 'En mantenimiento'),
        ('archived', 'Archivado'),
    ], string='Estado', default='available', required=True)
    
    _sql_constraints = [("name_uniq", "unique (name)", "El nombre del libro ya existe")]
    #nombre del sql constraints
    #unique () los valores que no queremos que se dupliquen
    #mensaje de error
        
    def btn_reservado(self):
        self.write({'state': 'reserved'})
    
    def btn_prestado(self):
        self.write({'state': 'loaned'})

    @api.depends('fecha_entrega', 'fecha_recibido')
    def _compute_dias_transcurridos(self):
        for record in self:
            if record.fecha_entrega and record.fecha_recibido:
                record.dias_transcurridos = (record.fecha_recibido - record.fecha_entrega).days
            else:
                record.dias_transcurridos = 0

class CategoriaLibro(models.Model):
    _name ='categoria.libro'
    _description = 'categoria de cada libro'
    
    name = fields.Char(string="Nombre de la categoría")
  
    