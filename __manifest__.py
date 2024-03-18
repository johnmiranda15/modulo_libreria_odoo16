# -- coding: utf-8 -*-
{
    'name': "Modulo para Libros",
    'summary': """Modulo para listar libros con sus autores""",
    'author': "Juan Quiroz",
    'category': "General",
    'version': '1.0.0',
    'depends': ['mail'],
    'data': [
        'views/menu_view.xml',
        'views/libros_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'report/libros_report.xml'
    ],
    'images': ['static/description/icon.png']
}