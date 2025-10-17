from odoo import http
from odoo.http import request
import os
import logging

# 用Odoo默认日志模块，避免ir.logging错误
_logger = logging.getLogger(__name__)

class WechatVerification(http.Controller):
    # 仅保留核心路由和文件读取
    @http.route('/WW_verify_bKh5CGfbqD7k5qGy.txt', 
                type='http', 
                auth='public', 
                website=True, 
                methods=['GET'])
    def verify_file(self):
        try:
            # 容器内的文件路径（固定，基于挂载关系）
            file_path = '/mnt/extra-addons/wechat_verification/static/WW_verify_bKh5CGfbqD7k5qGy.txt'
            
            # 1. 检查文件是否存在
            if not os.path.exists(file_path):
                _logger.warning(f"验证文件不存在: {file_path}")
                return request.make_response("File not found", status=404)
            
            # 2. 检查文件是否可读
            if not os.access(file_path, os.R_OK):
                _logger.warning(f"验证文件不可读: {file_path}")
                return request.make_response("Permission denied", status=403)
            
            # 3. 读取并返回文件（纯文本格式）
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            _logger.debug("验证文件访问成功")
            return request.make_response(
                content,
                [('Content-Type', 'text/plain; charset=utf-8')]
            )
        
        # 捕获所有异常，返回明确信息
        except Exception as e:
            _logger.error(f"验证文件处理错误: {str(e)}")
            return request.make_response(f"Error: {str(e)}", status=500)
