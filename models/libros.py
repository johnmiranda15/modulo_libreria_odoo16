from odoo import models, fields

#Creando un modelo ( tabla de datos) a partir de una clase
class Libros(models.Model):
    _name = 'libros' #nombre de la tabla que se va a generar
    _description = 'Informacion de cada libro'
    _inherit = ['mail.thread','mail.activity.mixin']
                
    name = fields.Char(string = "Nombre del libro", required=True, tracking=True) #nombre del campo que es de tipo cadena
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del Autor") 
    image = fields.Binary(string="Image")
    categoria_id = fields.Many2one(comodel_name='categoria.libro')
    state = fields.Selection([('draft','borrador'),('published','publicado')], default='draft')
    
    _sql_constraints = [("name_uniq", "unique (name)", "El nombre del libro ya existe")]
    #nombre del sql constraints
    #unique () los valores que no queremos que se dupliquen
    #mensaje de error
        
    def btn_publicar(self):
        self.write({'state': 'published'}) 
    
    def btn_borrador(self):
        self.write({'state': 'draft'})

class CategoriaLibro(models.Model):
    _name ='categoria.libro'
    
    name = fields.Char(string="Nombre de la categoría")
  
    