import requests

name = "E2021235"  # 自己写
password = "zx1012386834"  # 自己写

url = "http://10.10.8.162:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=%2C0%2C"+name+"&user_password="+password
# 发送 HTTP 请求
response = requests.get(url=url)
print(url)
print(response.text)

input("按下回车键退出. . .")
