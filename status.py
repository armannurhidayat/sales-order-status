from odoo import api, fields, models

class Status(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order' # Nama model yang ingin di sisipkan

    status_so = fields.Char(
    	string="Status",
    	required=True,
    	size=64, 
    )