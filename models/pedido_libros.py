"""pedido_libros"""

from odoo  import models, fields

class PedidoLibros(models.Model):
    """Clase Pedido de Libros"""
    _name = 'pedido.libros'
    _description = "Modelo de Libros para la librería"
    _rec_name = 'titulo'

    titulo = fields.Char(strinig="Titulo del Libro")
    autor = fields.Char(string="Autor/Editor")
    serie = fields.Char(string="Serie/Editorial")
    fecha_publicacion = fields.Date(string="Fecha de Publicación")
    isbn = fields.Char(string="ISBN")
    paginas = fields.Char(string="Páginas")
    tamano = fields.Char(string="Tamaño")
    precio = fields.Float(string="Precio")
    descuento = fields.Float(string="Descuento")
    link = fields.Char(string="Enlace Web")
    tipo_tapa = fields.Char(string="Tipo de Tapa")