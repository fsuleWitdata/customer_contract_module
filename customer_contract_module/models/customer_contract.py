from odoo import models, fields, api
from datetime import datetime

class CustomerContract(models.Model):
    _name = 'customer.contract'
    _description = 'Contrato con Cliente'
    
    name = fields.Char(string='Nombre', required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    description = fields.Text(string='Descripción', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha de Fin', required=True)
    total_hours = fields.Float(string='Horas Totales', required=True)
    completion_reason = fields.Text(string='Motivo de Finalización', help='Razón por la cual se completó antes de la fecha.')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Proceso'),
        ('completed', 'Terminado'),
    ], string='Estado', default='draft')

    @api.model
    def _compute_state(self):
        """Método para actualizar el estado basado en las fechas."""
        today = fields.Date.today()
        for contract in self:
            # Verificar si las fechas están definidas
            if contract.start_date and contract.end_date:
                if contract.state == 'draft' and contract.start_date <= today:
                    contract.state = 'in_progress'
                if contract.state != 'completed' and contract.end_date < today:
                    contract.state = 'completed'

    @api.model
    def create(self, vals):
        """Sobrescribimos el método create para ejecutar la comprobación cuando se crea un contrato."""
        contract = super(CustomerContract, self).create(vals)
        contract._compute_state()
        return contract

    @api.onchange('start_date', 'end_date')
    def _onchange_dates(self):
        """Verificamos las fechas cuando se cambian y actualizamos el estado."""
        self._compute_state()

    def set_in_progress(self):
        """Método que cambia el estado manualmente a 'in_progress' si la fecha de inicio es vigente."""
        self.state = 'in_progress'

    def set_completed(self):
        """Abrir wizard si se completa antes de la fecha."""
        today = fields.Date.today()
        for contract in self:
            if contract.end_date and today < contract.end_date:
                return {
                    'type': 'ir.actions.act_window',
                    'res_model': 'contract.completion.wizard',
                    'view_mode': 'form',
                    'target': 'new',
                    'context': {
                        'default_contract_id': contract.id,
                    },
                }
            else:
                contract.state = 'completed'
                
