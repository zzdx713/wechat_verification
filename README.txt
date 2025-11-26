该应用是为了解决企业微信域名验证而开发，在odoo18验证通过
下载企业微信的验证txt文件放到static中
修改controllers\mail.py将文件名WW_verify_bKh5CGfbqD7k5qGy.txt替换为下载的txt文件名
将该目录复制到addon目录登陆odoo安装企业微信验证应用
注意事项:如果修改记得重启服务
通过http://ip:端口/WW_verify_bKh5CGfbqD7k5qGy.txt
2025-11-26  一位朋友的环境为windows，更新代码支持windows odoo环境

