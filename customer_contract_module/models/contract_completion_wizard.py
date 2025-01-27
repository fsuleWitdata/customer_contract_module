from odoo import models, fields, api

class ContractCompletionWizard(models.TransientModel):
    _name = 'contract.completion.wizard'
    _description = 'Motivo de Finalización del Contrato'

    contract_id = fields.Many2one('customer.contract', string='Contrato', required=True)
    contract_name = fields.Char(string='Nombre del Contrato', related='contract_id.name', readonly=True)
    contract_id = fields.Many2one('customer.contract', string='Contrato', required=True)
    completion_reason = fields.Text(string='Motivo de Finalización', required=True)

    def confirm_reason(self):
        """Guardar el motivo en el contrato y cambiar el estado."""
        self.contract_id.write({
            'completion_reason': self.completion_reason,
            'state': 'completed',
        })
        return {'type': 'ir.actions.act_window_close'}
    