{
    'name': '企业微信验证模块',
    'version': '1.0',
    'author': 'Admin',
    'category': 'Tools',
    # 关键：依赖web模块（Odoo 18控制器需依赖）
    'depends': ['base', 'web'],
    'data': [],
    # 关键：允许安装+自动加载
    'installable': True,
    'auto_install': True,
    # 标记为应用，避免状态异常
    'application': False,
    'summary': '企业微信可信域名验证文件服务'
}
