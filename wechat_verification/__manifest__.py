{
    'name': '企业微信验证模块',
    'summary': """该应用是为了解决企业微信域名验证而开发在odoo18验证通过""",
    'description': """将该目录复制到addon目录登陆odoo安装企业微信验证应用，通过http://ip:端口/WW_verify_bKh5CGfbqD7k5qGy.txt""",
    'author': "zzdx713",
    'website': "https://github.com/zzdx713",
    'category': 'Tools',
    # 关键：依赖web模块（Odoo 18控制器需依赖）
    'version': '18.0',
    "license": "AGPL-3",
    'depends': ['base', 'web'],
    'data': [],
    # 关键：允许安装+自动加载
    'installable': True,
    'auto_install': True,
    # 标记为应用，避免状态异常
    'application': False,
    'summary': '企业微信可信域名验证文件服务',
    'images': [
        'static/description/icon.png',
    ]
}
