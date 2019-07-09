# Wechat-public-account-on-Raspberry-Pi
The WeChat public account based on flask is developed and deployed on the Raspberry Pi to realize hardware control and information collection.

### 介绍
简单搞了一下树莓派基于flask的微信公众号接口开发，部署在树莓派上完成设备控制以及信息采集。

### 软件架构
采用flask框架，可以运行在任意python环境下，但部分硬件设备的控制和数据的采集真对树莓派开发

### 运行效果
![硬件连接原理图](https://github.com/wangxu2016/Wechat-public-account-on-Raspberry-Pi/blob/master/others/img/Device_connection.png)
![硬件正面连接图](https://github.com/wangxu2016/Wechat-public-account-on-Raspberry-Pi/blob/master/others/img/RPi1.png)
![硬件侧面连接图](https://github.com/wangxu2016/Wechat-public-account-on-Raspberry-Pi/blob/master/others/img/RPi2.png)
![微信公众号效果图](https://github.com/wangxu2016/Wechat-public-account-on-Raspberry-Pi/blob/master/others/img/wecaht.png)

### 安装教程
下载代码：
```bash
git clone https://github.com/wangxu2016/Wechat-public-account-on-Raspberry-Pi.git
```
#### 配置修改：
修改`config.py`中的文件内容：

```python
# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    # 微信公众号appid
    APP_ID = 'wxfb561*******'
    # 微信公众号SECRET
    SECRET = '19078e4**********'
    # redis缓存
    REDIS_STORAGE = 'redis://127.0.0.1:6379/0'
    # 微信公众号认证的token
    WECHAT_TOKEN = 'wechat_token'
    # 放置脚本的位置，也就是现在others/code目录下的python脚本文件
    # 这些脚本文件运行在python2环境下，缺少相关类库的话自行下载
    CODE_PATH = '/home/pi/code/Wechat-public-account-on-Raspberry-Pi/others'

```
建议使用venv环境部署，其中flask使用的是python3的环境，亲测python3.5到3.7都是没有问题的，更低版本的python3环境理论是没有问题的
#### 下载相关python包：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
#### 线上环境启动flask：
```bash
gunicorn -w 5 -b 0.0.0.0:8102 --threads 6 manage:app
```
#### 测试环境启动：
```bash
 python manage.py runserver
```
这是设置的启动端口是`8102`可以根据自己的需求自定义，我的树莓派是内网ip，做了一下内网穿透，可以参考整理的[内网穿透](https://nknow.top/build-your-own-ngrok-intranet-penetration.html)进行配置。

#### 访问测试：
浏览器直接访问`http://127.0.0.1:8102/weixin`出现`错误的请求字样`，

#### 配置微信公众号
我这里为了方便直接使用的微信公众平台使用的测试号，直接把appid、secret配置在`config.py`文件中，`token`自定义，url跟上自定义的`域名或者ip:端口/weixin`配置成功后会有相关的的提示，前面要带上http或者https，80或者443端口可以省略。

#### 生成微信公众号菜单
`others`目录下的`set_menu.py`负责生成微信公众号菜单，配置`appid、secret`后直接运行即可生成相应的菜单，如有错误会有相应的返回码，查看微信公众号开发手册排查即可。

#### 异步电机
需要在`tasks.py`代码目录下启动`celery`:
```bash
celery -A tasks worker --loglevel=info
```
可以前面加`nohup`放到后台执行，也可以使用`screen`或者`tmux`放到后台执行，更高级一些可以使用`flower`监控，真对这个完全没有这个必要。