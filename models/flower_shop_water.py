from odoo import models,fields
from collections import defaultdict

class FlowerShopWater(models.Model):
    _name="flower.shop.water"
    _description="Flower Watering records"

    watering_date = fields.Date("Watering Date")
    lot_id = fields.Many2one('stock.lot')

    def action_needs_watering(self):
        flowers = self.env["product.template"].search([("is_flower", "=", True)])
        serials = self.env["stock.lot"].search([("product_id", "in", flowers.ids)])
        lot_vals = defaultdict(bool)
        for serial in serials:
            if serial.water_ids:
                last_watered_date = serial.water_ids[0].watering_date
                frequency = serial.product_id.flower_id.watering_frequency
                today = fields.Date.today()
                needs_watering = (today - last_watered_date).days >= frequency
                lot_vals[serial.product_id.id] |= needs_watering
            else:
                lot_vals[serial.product_id.id] = True
        for flower in flowers:
            flower.needs_watering = lot_vals[flower.id]

