# -*- coding: utf-8 -*-
from openerp import models, api


class account_analytic_account(models.Model):
    _name = 'account.analytic.account'
    _inherit = 'account.analytic.account'

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        import pdb; pdb.set_trace()

    @api.multi
    def pus_generate_invoice_data(self, period_id):
        ret = super(account_analytic_account, self).pus_generate_invoice_data(
            period_id)

        period = self.env['account.period'].browse(period_id)

        if not ret.get('journal_id', False):
            ret['journal_id'] = self.env['res.partner'].browse(
                ret['partner_id']).prefered_journals(
                    ret['type'])[ret['partner_id']][0]

        ret.update({
            'afip_service_start': period.date_start,
            'afip_service_end': period.date_stop,
        })

        return ret
