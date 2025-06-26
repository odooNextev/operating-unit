# © 2025 Nextev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        context = self.env.context.copy()
        context['origin_operating_unit'] = self.operating_unit_id.id
        self.env.context = context
        return super().action_confirm()
