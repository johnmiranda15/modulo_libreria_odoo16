"""importar_excel_de_libros"""

from odoo import models, fields, api
from odoo.exceptions import UserError
import xlrd
import tempfile
import binascii
import datetime
import time
import json


class ImportarDocumento(models.TransientModel):
    """Clase para Importar Documento de Excel"""
    _name = 'importar.documento'
    _description = "Subir Documento de Excel sobre pedido de Libros"
    _rec_name = "nombre_documento"

    archivo_importado = fields.Binary('Importar Archivo', required=True)
    nombre_documento = fields.Char('Nombre del Archivo')
    fecha_importacion = fields.Date('Fecha de Importación', default=fields.Date.today)

    @api.model
    def create(self, vals):
        if not vals.get('fecha_importacion'):
            vals['fecha_importacion'] = fields.Date.today()
        return super().create(vals)

    @staticmethod
    def excel_to_date(excel_serial):
        """Convierte una fecha en formato de número serial de Excel a un objeto `datetime.date`"""
        base_date = datetime.datetime(1899, 12, 30)
        delta = datetime.timedelta(days=excel_serial)
        return base_date + delta

    def importar_documento(self):
        """Función para importar y procesar un archivo Excel"""
        try:
            # Crear un archivo temporal para almacenar el archivo importado
            archivo_temporal = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            archivo_temporal.write(binascii.a2b_base64(self.archivo_importado))
            archivo_temporal.seek(0)
            archivo_temporal.close()
        except Exception:
            raise UserError("Archivo inválido")

        # Abrir el archivo Excel
        try:
            libro_excel = xlrd.open_workbook(archivo_temporal.name, on_demand=True)
            hoja = libro_excel.sheet_by_index(0)
        except Exception as e:
            raise UserError(f"Error al abrir el archivo Excel: {str(e)}")

        # Verificar si hay columnas en la hoja
        if hoja.ncols == 0:
            raise UserError("El archivo Excel no contiene columnas.")

        # Obtener los nombres de las columnas en la primera fila
        primera_fila = []
        for col in range(hoja.ncols):
            primera_fila.append(hoja.cell_value(0, col))

        # Procesar las filas de datos
        lineas_importadas = []
        for fila in range(1, hoja.nrows):
            lineas = {}
            for col in range(hoja.ncols):
                lineas[primera_fila[col]] = hoja.cell_value(fila, col)
            lineas_importadas.append(lineas)

        # Lista para almacenar los IDs de los registros de libros creados
        libros_ids = []
        for importacion in lineas_importadas:
            fecha_publicacion_excel = importacion.get('Año de publicacion')
            # Verificamos si cada valor es float por separado
            if isinstance(fecha_publicacion_excel, float):
                fecha_publicacion = self.excel_to_date(fecha_publicacion_excel).date()
            else:
                # Verificamos que la fecha no sea una cadena vacía o solo espacios
                fecha_publicacion = fields.Date.from_string(
                    fecha_publicacion_excel.strip()) if fecha_publicacion_excel and fecha_publicacion_excel.strip() else None
            # Crear registro en el modelo libros librería
            libros_ids.append(self.env['pedido.libros'].create({
                'titulo': str(importacion.get('Titulo')) or '',
                'autor': str(importacion.get('Autor/editor')) or '',
                'serie': str(importacion.get('Serie/Editorial')) or '',
                'fecha_publicacion': fecha_publicacion,
                'isbn': str(importacion.get('ISBN')) or '',
                'paginas': str(importacion.get('Paginas')) or '',
                'tamano': str(importacion.get('Tamaño')) or '',
                'precio': float(importacion.get('Precio Lista (dolares)', 0.0)),
                'descuento': float(importacion.get('Descuento', 0.0)),
                'link': str(importacion.get('Web page link')) or '',
                'tipo_tapa': str(importacion.get('DISPONIBLE')) or '',
            }).id)

        # Retornar Notificación de éxito
        return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Éxito',
                    'message': 'Documento subido con éxito.',
                    'type': 'success',  # success, warning, danger, info
                    'sticky': False,  # Si True, la notificación se mantendrá visible
                }
            }
