# -*- coding: utf-8 -*-
from odoo import fields, models


class TaskTemplate(models.Model):
    """Create a class model for task template"""
    _name = 'task.template'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    project_id = fields.Many2one('project.template', string='Project')
    user_ids = fields.Many2many('res.users', string='Assigned to')
    deadline = fields.Date(string='Deadline')
    tags_ids = fields.Many2many('project.tags', string='Tags')
    description = fields.Text(string='Description', translate=True)
    partner_id = fields.Many2one('res.partner',
                                 string='Customer')
    company_id = fields.Many2one('res.company', string='Company')
    sequence = fields.Integer(string='Sequence')
    email_cc = fields.Char(string='Email cc')
    date_assign = fields.Datetime(string='Assigning Date')
    date_last_stage_update = fields.Datetime(string='Last Stage Update')

    def create_task(self):
        """function for creating new task"""
        task_values = {
            'name': self.name,
            'user_ids': self.user_ids.ids,
            'partner_id': self.partner_id.id,
            'date_deadline': self.deadline,
            'tag_ids': self.tags_ids.ids,
            'sequence': self.sequence,
            'date_assign': self.date_assign,
            'date_last_stage_update': self.date_last_stage_update
        }

        if self.project_id:
            project = self.env['project.project'].search(
                [('name', '=', self.project_id.name)])
            task_values['project_id'] = project.id

        task = self.env['project.task'].create(task_values)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'form',
            'res_id': task.id,
            'target': 'current',
        }
