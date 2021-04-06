from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    industry_id = fields.Many2one(related='partner_id.industry_id', store=True, string='Industria')