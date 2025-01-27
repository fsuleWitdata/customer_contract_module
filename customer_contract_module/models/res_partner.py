from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    partner_id_customer_contract_count = fields.Integer(
        string="Contracts Count", 
        compute='compute_customer_contract_count', 
        default=0
    )
    
    def compute_customer_contract_count(self):
        for record in self:
            record.partner_id_customer_contract_count = self.env['customer.contract'].search_count([
                ('partner_id', '=', record.id)
            ])
    
    def action_view_customer_contracts(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contracts',
            'res_model': 'customer.contract',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.id)],
            'context': {'create': False},
        }
