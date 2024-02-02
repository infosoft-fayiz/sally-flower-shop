from odoo import models,fields,api
from odoo.exceptions import ValidationError, UserError
from datetime import date

class StockLot(models.Model):
    _inherit = 'stock.lot'

    water_ids = fields.One2many('flower.shop.water', 'lot_id')
    is_flower = fields.Boolean("Is Flower", related='product_id.is_flower')

    def action_water_flower(self):
        flowers = self.browse([])
        for record in self: 
            if record.is_flower:
                flowers += record   
        for record in flowers:
            if record.water_ids:
                last_watered_date = record.water_ids[0].watering_date
                frequency = record.product_id.flower_id.watering_frequency
                if (date.today() - last_watered_date).days < frequency:
                    continue
            self.env['flower.shop.water'].create({
                'watering_date': date.today(),
                'lot_id': self.id
            })
            

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product = self.env['product.product'].browse(vals["product_id"])
            if product.sequence_id:
                vals['name'] = product.product_tmpl_id.sequence_id.next_by_id()
        return super().create(vals_list)

