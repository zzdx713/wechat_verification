# -*- coding: utf-8 -*-
{
    'name': "Odoo-钉钉",
    'summary': """该应用是为了解决企业微信域名验证而开发在odoo18验证通过""",
    'description': """将该目录复制到addon目录登陆odoo安装企业微信验证应用，通过http://ip:端口/WW_verify_bKh5CGfbqD7k5qGy.txt""",
    'author': "XueFeng.Su",
    'website': "https://github.com/cd-feng",
    'category': 'Dingtalk/HR',
    'version': '18.0.0.1',
    'depends': ['hr'],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/default_ir_cron.xml',

        'views/menu.xml',
        'views/dingtalk_setting.xml',
        'views/hr_department.xml',
        'views/hr_employee.xml',
        'views/res_users.xml',

        'wizard/hr_department_wizard.xml',
        'wizard/hr_employee_wizard.xml',
    ],
    'images': [
        'static/description/image_1.png',
    ],
}
