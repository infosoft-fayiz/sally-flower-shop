from odoo import models,fields

class FlowerShop(models.Model):
    _name = 'flower.shop'
    _description = "Sally's Flower Shop"

    common_name = fields.Char(string='Common Name', required=True)
    scientific_name = fields.Char(string='Scientific Name', required=True)
    season_start = fields.Date(string='Season Start')
    season_end = fields.Date(string='Season End')
    watering_frequency = fields.Integer(string='Watering Frequency (days)')
    watering_amount = fields.Float(string='Watering Amount (ml)')

    def name_get(self):
        return [(flower.id, "{} ({})".format(flower.scientific_name, flower.common_name)) for flower in self]