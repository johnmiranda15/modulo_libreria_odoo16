"""libros_libreria"""

from odoo  import models, fields

class LibrosLibreiaIglesia(models.Model):
    """Clase Libros de la Libreria de la Iglesia"""
    _name = 'libros.libreria'
    _description = "Modelo de Libros para la librería"
    _rec_name = 'titulo'

    titulo = fields.Char(strinig="Titulo del Libro")
    autor = fields.Char(string="Autor/Editor")
    serie = fields.Char(string="Serie/Editorial")
    fecha_publicacion = fields.Date(string="Fecha de Publicación")
    isbn = fields.Char(string="ISBN")
    pagina = fields.Char(string="Páginas")
    tamano = fields.Char(string="Tamaño")
    precio = fields.Float(string="Precio")
    descuento = fields.Float(string="Descuento")
    link = fields.Char(string="Enlace Web")
    tipo_tapa = fields.Char(string="Tipo de Tapa")