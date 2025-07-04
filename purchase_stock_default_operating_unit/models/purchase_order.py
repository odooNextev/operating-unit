# © 2025 Nextev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _prepare_picking(self):
        res = super()._prepare_picking()
        if self.operating_unit_id:
            res["operating_unit_id"] = self.operating_unit_id.id
        return res
