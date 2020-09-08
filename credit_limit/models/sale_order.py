# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

from odoo.exceptions import UserError, AccessError


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'
    
    credit_limit_block = fields.Boolean(copy=False)
    
    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)        
        result.credit_limit_check()
        return result
    
    @api.multi
    def action_confirm(self):
        for order in self:
            if order.credit_limit_block:
                raise UserError(_('Order %s is blocked because of credit limit') % order.name)
        return super(SaleOrder, self).action_confirm()
    
    @api.one
    def credit_limit_check(self):
        is_exceeded =self.credit_limit_exceeded()
        if is_exceeded and is_exceeded[0]:
            self.credit_limit_block = True
            # use oca module web_notify to notify user
            self.env.user.notify_warning(_('Order is blocked because of credit limit'))
            
    @api.one
    def credit_limit_exceeded(self):
        """
        If the total amount of the current order plus partner credit(open amounts from invoices)
        bigger than partner credit limit, we consider it as credit limit exceeded
        """
        if self.partner_id and self.partner_id.use_credit_limit:
            if (self.partner_id.credit + self.amount_total) > self.partner_id.credit_limit:
                return True
        return False
                    
