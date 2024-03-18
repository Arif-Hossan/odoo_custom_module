# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient Information"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default="draft", string="Status", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible")

    def action_confirm(self):
        self.state = 'confirm'

    # def action_done(self):
    #     if self.state == 'draft' or self.state == 'confirm':
    #         self.state = 'done'
    def action_done(self):
        for record in self:
            if record.state in ('draft', 'confirm'):
                record.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
