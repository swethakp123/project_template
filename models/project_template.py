# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTemplate(models.Model):
    """create a new model on project template"""
    _name = 'project.template'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    label_tasks = fields.Char(string='Name of the tasks')
    user_id = fields.Many2one('res.users', string='Project Manager')
    partner_id = fields.Many2one('res.partner', string='Customer')
    company_id = fields.Many2one('res.company', string='Company')
    description = fields.Text(string='Description', translate=True)
    privacy_visibility = fields.Selection([
        ('followers', 'Invited internal users'),
        ('employees', 'All internal users'),
        ('portal', 'Invited portal users and all internal users'),
    ],
        string='Visibility', required=True,
        default='portal')
    allocated_hours = fields.Float(string='Allocated Hours')
    tasks_ids = fields.One2many('task.template',
                                'project_id', string='Tasks')

    def create_project(self):
        """ function for creating new project on project template"""
        project_values = {
            'name': self.name,
            'description': self.description,
            'label_tasks': self.label_tasks,
            'user_id': self.user_id.id,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'privacy_visibility': self.privacy_visibility,
            'task_ids': [(fields.Command.create({
                'name': task.name,
                'user_ids': task.user_ids.ids,
                'date_deadline': task.deadline,
                'tag_ids': task.tags_ids.ids,
                'sequence': task.sequence,
                'date_assign': task.date_assign,
                'date_last_stage_update': task.date_last_stage_update,
                'email_cc': task.email_cc
            })) for task in self.tasks_ids]
        }
        project = self.env['project.project'].create(project_values)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': project.id,
            'target': 'current',
        }
