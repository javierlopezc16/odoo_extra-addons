# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    industry_id = fields.Many2one(related='partner_id.industry_id', store=True, string='Industry')


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    industry_id = fields.Many2one(related='partner_id.industry_id', store=True, string='Industry')
