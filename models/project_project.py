# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectProject(models.Model):
    """create a class for project module"""
    _inherit = 'project.project'

    project_template_id = fields.Many2one('project.template',
                                          string='Project Template')

    def create_project_template(self):
        """Function for creating project template"""
        project_values = {
            'name': self.name,
            'description': self.description,
            'label_tasks': self.label_tasks,
            'user_id': self.user_id.id,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'privacy_visibility': self.privacy_visibility,
            'tasks_ids': [(fields.Command.create({
                'name': task.name,
                'user_ids': task.user_ids.ids,
                'deadline': task.date_deadline,
                'tags_ids': task.tag_ids.ids,
                'sequence': task.sequence,
                'date_assign': task.date_assign,
                'date_last_stage_update': task.date_last_stage_update,
                'email_cc': task.email_cc
            })) for task in self.task_ids]
        }
        project = self.env['project.template'].create(project_values)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.template',
            'view_mode': 'form',
            'res_id': project.id,
            'target': 'current',
        }
