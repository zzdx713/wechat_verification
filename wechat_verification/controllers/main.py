from odoo import http
from odoo.http import request
import os
import logging
import sys

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
            # 跨平台文件路径处理
            if sys.platform == 'win32':
                # Windows环境：使用相对路径或绝对路径
                # 方案1：相对于当前模块的路径
                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, '..', 'static', 'WW_verify_bKh5CGfbqD7k5qGy.txt')
                file_path = os.path.normpath(file_path)
                
                # 方案2：如果方案1不行，尝试使用绝对路径（根据你的实际安装位置修改）
                # file_path = r'C:\path\to\your\odoo\addons\wechat_verification\static\WW_verify_bKh5CGfbqD7k5qGy.txt'
            else:
                # Linux/Docker环境：保持原有路径
                file_path = '/mnt/extra-addons/wechat_verification/static/WW_verify_bKh5CGfbqD7k5qGy.txt'
            
            _logger.info(f"尝试访问验证文件: {file_path}")
            
            # 1. 检查文件是否存在
            if not os.path.exists(file_path):
                _logger.warning(f"验证文件不存在: {file_path}")
                # 在Windows上尝试其他可能的位置
                if sys.platform == 'win32':
                    # 尝试Odoo标准addons路径
                    alternative_path = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 
                                                  'wechat_verification', 'static', 'WW_verify_bKh5CGfbqD7k5qGy.txt')
                    alternative_path = os.path.normpath(alternative_path)
                    _logger.info(f"尝试备用路径: {alternative_path}")
                    if os.path.exists(alternative_path):
                        file_path = alternative_path
                        _logger.info(f"使用备用路径: {file_path}")
                    else:
                        return request.make_response("File not found", status=404)
                else:
                    return request.make_response("File not found", status=404)
            
            # 2. 检查文件是否可读
            if not os.access(file_path, os.R_OK):
                _logger.warning(f"验证文件不可读: {file_path}")
                return request.make_response("Permission denied", status=403)
            
            # 3. 读取并返回文件（纯文本格式）
            # 处理Windows和Linux的编码差异
            encodings = ['utf-8', 'gbk', 'gb2312', 'utf-8-sig']
            content = None
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    _logger.debug(f"使用编码 {encoding} 成功读取文件")
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                _logger.error("无法使用任何编码读取文件")
                return request.make_response("Encoding error", status=500)
                
            _logger.debug("验证文件访问成功")
            return request.make_response(
                content,
                [('Content-Type', 'text/plain; charset=utf-8')]
            )
        
        # 捕获所有异常，返回明确信息
        except Exception as e:
            _logger.error(f"验证文件处理错误: {str(e)}")
            return request.make_response(f"Error: {str(e)}", status=500)
