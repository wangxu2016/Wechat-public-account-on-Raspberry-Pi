from wechatpy import WeChatClient

# 代码运行之后生成相应的菜单

# 这里填写appid和secret
client = WeChatClient('wxfb561a9de0e******', '19078e4488932d02**********')
client.menu.delete()
status = client.menu.create(
    {
        "button": [
            {
                "name": "控制",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "开灯",
                        "key": "on_light"
                    },
                    {
                        "type": "click",
                        "name": "关灯",
                        "key": "off_light"
                    },
                    {
                        "type": "click",
                        "name": "开窗帘",
                        "key": "on_curtain"
                    },
                    {
                        "type": "click",
                        "name": "关窗帘",
                        "key": "off_curtain"
                    },
                    {
                        "type": "click",
                        "name": "实况拍摄",
                        "key": "monitor"
                    },

                ]
            },
            {
                "name": "实时",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "设备状况",
                        "url": "http://dashboard.proxys.nknow.top/"
                    },
                    {
                        "type": "view",
                        "name": "室内监控",
                        "url": "http://sv.proxys.nknow.top/"
                    },
                    {
                        "type": "click",
                        "name": "房间温度",
                        "key": "temperature"
                    },
                    {
                        "type": "click",
                        "name": "房间湿度",
                        "key": "humidity"
                    },
                    {
                        "type": "click",
                        "name": "people",
                        "key": "people"
                    }
                ]
            },
            {
                "name": "其他",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "智能助手",
                        "url": "http://robot.proxys.nknow.top/"
                    },
                    {
                        "type": "view",
                        "name": "cloud",
                        "url": "http://cloud.proxys.nknow.top/"
                    },
                    {
                        "type": "view",
                        "name": "关于",
                        "url": "http://about.proxys.nknow.top/"
                    }
                ]
            }
        ]
    }
)
print(status)
