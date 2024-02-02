from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_flower = fields.Boolean(string='Is a Flower')
    flower_id = fields.Many2one('flower.shop', string="Flower Type")
    sequence_id = fields.Many2one('ir.sequence', string="Flower Sequence")    
    gardeners_ids = fields.Many2many('res.users')
    needs_watering = fields.Boolean(default=False)