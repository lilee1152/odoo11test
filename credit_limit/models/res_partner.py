# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    use_credit_limit = fields.Boolean()
    credit_limit = fields.Monetary()
    # if use_credit_limit and (credit + amount_total of a new sale order) < credit_limit, block the sale order
    
