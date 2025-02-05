# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).


from odoo import models, fields, api, _


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    state = fields.Selection(selection_add=[('refund', 'Refund')])

    def _send_mail(self):
        self.ensure_one()
        template = self.env.ref(
            'smile_event_refund_registration.refund_event_registration', False)
        template.send_mail(self.id, force_send=True)

    @api.model
    def prepare_account_invoice(self, invoice_id):
        """
         Prepare values
        """
        values = invoice_id.copy_data()[0]
        values.update({'name': _('Event refund')})
        return values

    def button_cancel_refund(self):
        """
        Cancel  and refund registration
        """
        for record in self:
            return record._process_event_refund()

    def _process_event_refund(self):
        """
         Process event refund
        """
        self.ensure_one()
        # create refund
        state = 'cancel'
        order = self.sale_order_id
        if order:
            if order.state in ('draft', 'sent'):
                order.action_cancel()
            # when invoicing
            for invoice in order.invoice_ids:
                if invoice.state == 'draft':
                    invoice.button_cancel()
                elif invoice.state == 'posted':
                    # Create refund
                    values = self.prepare_account_invoice(invoice)
                    self.env['account.move'].create(values)
                    state = 'refund'
        # Send mail
        self._send_mail()
        # Update event
        self.state = state
