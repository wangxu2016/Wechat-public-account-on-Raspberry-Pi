import subprocess
import datetime
from dateutil import tz


class PiSysCall(object):

    def __init__(self, path_info):
        self.path = path_info + '/'

    # 系统调用
    def sys_call(self, command):
        # command 命令字符串
        # ["echo '123'"]
        # 执行结果列表数据
        tmp = subprocess.check_output(command, shell=True)
        return tmp.decode('utf8').strip().split('\n')

    # 开灯
    def on_light(self):
        # 开灯相关操作
        try:
            command = ['python {} {}'.format(self.path + 'light.py', 'on')]
            self.sys_call(command)
            return "灯已打开"
        except Exception as e:
            return '操作失败'

    # 关灯
    def off_light(self):
        # 关灯相关操作
        try:
            command = ['python {} {}'.format(self.path + 'light.py', 'off')]
            self.sys_call(command)
            return "灯已关闭"
        except Exception as e:
            return '操作失败'

    # 温度
    def temperature(self):
        try:
            command = ['python {}'.format(self.path + 'temperature.py')]
            celsius = self.sys_call(command)
            return "当前温度" + str(celsius[0]) + "℃"
        except Exception as e:
            return '操作失败'

    # 湿度
    def humidity(self):
        try:
            command = ['python {}'.format(self.path + 'humidity.py')]
            dampness = self.sys_call(command)
            return "当前湿度" + str(dampness[0]) + "%"
        except Exception as e:
            return '操作失败'

    # 监控[当前状况拍摄照片返回]
    def monitor(self):
        tz_sh = tz.gettz('Asia/Shanghai')
        name = 'vs-{}.jpg'.format(datetime.datetime.now(tz=tz_sh).strftime('%Y-%m-%d-%H:%M:%S.%f'))
        img_file = self.path + 'images/' + name
        try:
            command = ['fswebcam --no-banner -r 640x480 {}'.format(img_file)]
            self.sys_call(command)
            return img_file
        except Exception as e:
            print(e)
            return '操作失败'

    # 调用步进电机开窗帘
    def on_curtain(self):
        try:
            command = ['python {}'.format(self.path + 'tasks.py on')]
            dampness = self.sys_call(command)
            return dampness[0]
        except Exception as e:
            return '操作失败'

    # 调用步进电机关窗帘
    def off_curtain(self):
        try:
            command = ['python {}'.format(self.path + 'tasks.py off')]
            dampness = self.sys_call(command)
            return dampness[0]
        except Exception as e:
            return '操作失败'

    # 判断房间是否有人
    def people(self):
        try:
            command = ['python {}'.format(self.path + 'people.py')]
            dampness = self.sys_call(command)
            if dampness[0] == 'yes':
                return "房间有人"
            else:
                return "房间无人"
        except Exception as e:
            return '操作失败'


if __name__ == '__main__':
    path = '/home/pi/code'
    exam = PiSysCall(path).humidity()
    print(exam)
