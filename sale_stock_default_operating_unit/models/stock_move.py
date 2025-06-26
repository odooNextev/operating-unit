# © 2025 Nextev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import _, api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        operating_unit_id = self.env.context.get('origin_operating_unit', False)
        res = super()._get_new_picking_values()
        res['operating_unit_id'] = operating_unit_id
        return res

    def _check_stock_move_operating_unit(self):
        return True