# -*- coding: utf-8 -*-
{
    'name': "Project Template",
    'version': '17.0.1.0.0',
    'depends': ['project'],
    'category': 'Project',
    'description': """
    This app allows project team to create project template and task template.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/project_template_view.xml',
        'views/task_template.xml',
        'views/project_project_view.xml',
        'views/project_task.xml',
    ],
    'application': 'True',
    'installable': True,
}
