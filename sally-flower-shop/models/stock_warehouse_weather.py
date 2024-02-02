from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import ValidationError
import requests

class FlowerShopWeather(models.Model):
    _name = 'flower.shop.weather'
    _description = 'weather checking for plants'

    warehouse_id = fields.Many2one('stock.warehouse')
    temperature = fields.Float("Temperature")
    pressure = fields.Float()
    humidity = fields.Float()
    wind_speed = fields.Float()
    rain_volume = fields.Float()
    description = fields.Char()
    capture_time = fields.Datetime()
    
class warehouse(models.Model):
    _inherit = 'stock.warehouse'

    weather_ids = fields.One2many('flower.shop.weather', 'warehouse_id')
    
    def _get_api_key_and_location(self, show_error):
        api_key = self.env["ir.config_parameter"].sudo().get_param("flower_shop.weather_api_key")
        if api_key == "unset" or not api_key:
            show_error(True)
        return api_key

    def get_weather(self, show_error=True):
        self.ensure_one()
        api_key = self._get_api_key_and_location(show_error)
        url = "https://api.openweathermap.org/data/2.5/weather?lat=25.2582&lon=55.3047&appid={}".format(api_key)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            entries = response.json()
            self.env["flower.shop.weather"].create({
                "warehouse_id": self.id,
                "description": entries["weather"][0]["description"],
                "pressure": entries["main"]["pressure"],
                "temperature": entries["main"]["temp"],
                "humidity": entries["main"]["humidity"] / 100,
                "wind_speed": entries["wind"]["speed"],
                "rain_volume": entries["rain"]["1h"] if "rain" in entries else 0,
                "capture_time": fields.Datetime.now(),
            })
        except Exception as e:
            raise ValidationError(e)

    def get_weather_all(self):
        for warehouse in self.search([]):
            warehouse.get_weather(show_error=False)

    def get_forecast_all_warehouses(self, show_error=True):
        flower_serials_to_water = self.env["stock.lot"]
        for warehouse in self:
            api_key = warehouse._get_api_key_and_location(show_error)
            url = "https://api.openweathermap.org/data/2.5/weather?lat=25.2582&lon=55.3047&appid={}".format(api_key)
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                entries = response.json()
                is_rainy_today = False
                # check only first 4 items in the list from 9 AM to 6 PM
                for i in range(0, 4):
                    if "rain" in entries["list"][i]:
                        rain = entries["list"][i]["rain"]["3h"]
                        if rain > 0.2:
                            is_rainy_today = True
                            break
                if is_rainy_today:
                    flower_products = self.env["product.product"].search([("is_flower", "=", True)])
                    quants = self.env["stock.quant"].search([
                        ("product_id", "in", flower_products.ids),
                        ("location_id", "=", warehouse.lot_stock_id.id)
                    ])
                    flower_serials_to_water |= quants.lot_id
            except Exception as e:
                ValidationError(e)
        for flower_serial in flower_serials_to_water:
            self.env["flower.water"].create({
                "serial_id": flower_serial.id,
            })