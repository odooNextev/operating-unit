from odoo import models


class StockLocation(models.Model):
    _inherit = "stock.location"

    def _check_required_operating_unit(self):
        return True
