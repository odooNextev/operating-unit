from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockLocation(models.Model):
    _inherit = "stock.location"

    def _check_required_operating_unit(self):
        return True