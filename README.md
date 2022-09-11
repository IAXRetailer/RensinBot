# ReisenBot

## How to start

### 安装前置环境

#### 安装Python

推荐使用版本Python3.8.10

https://www.python.org/downloads/release/python-3810/

直链 https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe

安装时候记得勾选把python加入环境变量，否则可能会出现意料之外的错误
#### 安装依赖

打开cmd运行

```sh
pip uninstall nonebot
pip install nb-cli
```
### 编辑配置

#### 编辑.env.dev
```cfg
SUPERUSERS=["超级用户qq_1","超级用户qq_2"]
NICKNAME=["Bot名称1","Bot名称2"]
```
#### 初始化

运行go-cqhttp.exe

选择反向websocket连接，编辑config.yml

```yml
  uin: 123456 # 改为你的QQ账号
  password: '你的密码' # 密码为空时使用扫码登录

  ...

  - ws-reverse:
      # 反向WS Universal 地址
      # 注意 设置了此项地址后下面两项将会被忽略
      universal: ws://127.0.0.1:8080/onebot/v11/ws/
```

编辑完毕后关闭exe，然后运行 '运行bot.bat' 或者根据下方教程使用手动启动

- 运行go-cqhttp.exe
- powershell或cmd运行**nb run**

扫码登录后应该就能够使用bot相关功能


