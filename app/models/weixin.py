from wechatpy.session.redisstorage import RedisStorage
from wechatpy.client import WeChatClient
from redis import Redis
from wechatpy.replies import TextReply
from flask import current_app
from .syscall import PiSysCall


class MenuClick(object):
    def __init__(self, msg, ):
        self.msg = msg
        self.path = current_app.config['CODE_PATH'],
        redis_client = Redis.from_url(current_app.config['REDIS_STORAGE'])
        session_interface = RedisStorage(
            redis_client,
            prefix="ACCESS_TOKEN"
        )
        self.client = WeChatClient(
            current_app.config['APP_ID'],
            current_app.config['SECRET'],
            session=session_interface
        )

    # 根据点击的按钮实际完成相应的操作
    def menu_click(self):
        try:
            return getattr(self, self.msg.key)()
        except Exception as e:
            print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
            print('错误所在的行号：', e.__traceback__.tb_lineno)
            print(e)
            return self.return_text("未知操作")

    # 开灯
    def on_light(self):
        text = PiSysCall(self.path[0]).on_light()
        # 开灯相关操作
        return self.return_text(text)

    # 关灯
    def off_light(self):
        text = PiSysCall(self.path[0]).off_light()
        # 开灯相关操作
        return self.return_text(text)

    # 温度
    def temperature(self):
        celsius = PiSysCall(self.path[0]).temperature()
        return self.return_text(celsius)

    # 湿度
    def humidity(self):
        celsius = PiSysCall(self.path[0]).humidity()
        return self.return_text(celsius)

    # 监控[当前状况拍摄照片返回]
    def monitor(self):
        self.send_img()
        return self.return_text("请点击查看实况拍摄照片")

    # 关闭窗帘
    def off_curtain(self):
        text = PiSysCall(self.path[0]).off_curtain()
        # text = "窗帘已关闭"
        return self.return_text(text)

    # 打开窗帘
    def on_curtain(self):
        text = PiSysCall(self.path[0]).on_curtain()
        # text = "窗帘已打开"
        return self.return_text(text)

    # 反馈是否有人
    def people(self):
        text = PiSysCall(self.path[0]).people()
        if "有人" in text:
            self.send_img()
        return self.return_text(text)

    # 描述性文字
    def return_text(self, text):
        reply = TextReply(message=self.msg)
        reply.content = text
        # 转换成 XML
        xml = reply.render()
        return xml

    # 发送照片
    def send_img(self):
        # 调用系统函数
        # 拍照截图 图片为类型+时间戳.jpg
        # img_file = "类型+时间戳.jpg"
        img_file = PiSysCall(self.path[0]).monitor()
        img = open(img_file, 'rb')
        img_upload = self.client.media.upload('image', img)
        self.client.message.send_image(self.msg.source, img_upload['media_id'])
