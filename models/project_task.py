# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    """create a class for project task model"""
    _inherit = 'project.task'

    task_template_id = fields.Many2one(string='Task Template')

    def create_task_template(self):
        """ function for creating new task template"""
        task_values = {
            'name': self.name,
            'user_ids': self.user_ids.ids,
            'partner_id': self.partner_id.id,
            'deadline': self.date_deadline,
            'tags_ids': self.tag_ids.ids,
            'sequence': self.sequence,
            'date_assign': self.date_assign,
            'date_last_stage_update': self.date_last_stage_update
        }
        if self.project_id:
            project = self.env['project.template'].search(
                [('name', '=', self.project_id.name)])
            task_values['project_id'] = project.id

        task = self.env['task.template'].create(task_values)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'task.template',
            'view_mode': 'form',
            'res_id': task.id,
            'target': 'current',
        }
