import requests
import subprocess
import re

# 执行 shell 命令来获取网络适配器的 IP 地址
result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)
# 打印输出以进行调试
print(result.stdout)

# 修改正则表达式以匹配输出格式
match1 = re.search(r'以太网适配器 以太网:[\s\S]*?IPv6 地址[ .]*: ([0-9a-fA-F:]+)', result.stdout)
match2 = re.search(r'无线局域网适配器 以太网:[\s\S]*?IPv6 地址[ .]*: ([0-9a-fA-F:]+)', result.stdout)


def f(match):
    ip = match.group(1)
    print(f'IP Address: {ip}')

    name = "E2021235"  # 自己写
    password = "zx1012386834"  # 自己写

    url = "http://10.10.8.162:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=%2C0%2C"+name+"&user_password="+password+"&wlan_user_ip=" + ip +"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2.2&terminal_type=1&lang=zh-cn&v=9024&lang=zh"
    # 发送 HTTP 请求
    response = requests.get(url=url)
    print(url)
    print(response.text)


if match1:
    f(match1)
elif match2:
    f(match2)
else :
    print('No IP address found.')
input("按下回车键退出. . .")
