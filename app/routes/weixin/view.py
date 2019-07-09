from . import bp
from flask import request
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import TextReply
from wechatpy import parse_message
from app.models.weixin import MenuClick
from flask import current_app
from flask.views import MethodView


@bp.route('/', methods=['GET', 'POST'])
class WechatView(MethodView):
    def get(self):
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echo_str = request.args.get('echostr', '')
        try:
            check_signature(current_app.config['WECHAT_TOKEN'],
                            signature, timestamp, nonce)
        except InvalidSignatureException:
            echo_str = '错误的请求'
        return echo_str

    def post(self):
        msg = parse_message(request.data)
        # 是文本消息
        if msg.type == 'text':
            reply = TextReply(message=msg)
            reply.content = 'text reply'
            xml = reply.render()
            return xml
        # 事件类型消息
        elif msg.type == 'event':
            # 处理菜单点击事件
            if msg.event == 'click':
                # MenuClick是自定义类，处理菜单点击事件
                click = MenuClick(msg)
                return click.menu_click()
            # 其他类型的事件消息不处理
            else:
                reply = TextReply(message=msg)
                reply.content = 'event未知'
                xml = reply.render()
                return xml
        # 其他消息
        else:
            reply = TextReply(message=msg)
            reply.content = '未知操作'
            xml = reply.render()
            return xml
# 收到的消息和发送者openid
        # print(msg.content)
        # print(msg.source)
# app.add_url_rule('/wechat/', view_func=WechatView.as_view('wechat'))
# def wechat():
#     if request.method == 'GET':
#         signature = request.args.get('signature', '')
#         timestamp = request.args.get('timestamp', '')
#         nonce = request.args.get('nonce', '')
#         echo_str = request.args.get('echostr', '')
#         try:
#             check_signature(current_app.config['WECHAT_TOKEN'], signature, timestamp, nonce)
#         except InvalidSignatureException:
#             echo_str = '错误的请求'
#         return echo_str
#     else:
#         msg = parse_message(request.data)
#         # 收到的消息和发送者openid
#         # print(msg.content)
#         # print(msg.source)
#         if msg.type == 'text':
#             reply = TextReply(message=msg)
#             reply.content = 'text reply'
#             # 转换成 XML
#             xml = reply.render()
#             return xml
#         elif msg.type == 'event':
#             if msg.event == 'click':
#                 click = MenuClick(msg)
#                 return click.menu_click()
#             else:
#                 reply = TextReply(message=msg)
#                 reply.content = 'event未知'
#                 xml = reply.render()
#                 return xml
#         else:
#             reply = TextReply(message=msg)
#             reply.content = '未知'
#             # 转换成 XML
#             xml = reply.render()
#             return xml
