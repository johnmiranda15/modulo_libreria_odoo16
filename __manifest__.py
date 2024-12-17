# -- coding: utf-8 -*-
{
    'name': "Modulo para Libros",
    'summary': """Modulo para listar libros con sus autores""",
    'author': "Juan Quiroz",
    'category': "General",
    'version': '1.0.0',
    'depends': ['mail'],
    'data': [
        'views/libros_biblioteca_view.xml',
        'views/pedido_libros_view.xml',
        'views/autores_view.xml',
        'views/accion_servidor_importar_documento.xml',
        'views/importar_documento_view.xml',
        'views/usuarios_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        #'report/libros_report.xml'
    ],
    'images': ['static/description/icon.png']
}