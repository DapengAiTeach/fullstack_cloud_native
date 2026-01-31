import requests

# 测试访问A
try:
    resp = requests.get("http://ch06_demo03_a:8000/")
    print("访问A服务成功:", resp.json())
except Exception as e:
    print("访问A服务失败:", e)

# 测试访问B
try:
    resp = requests.get("http://ch06_demo03_b:8000/")
    print("访问B服务成功:", resp.json())
except Exception as e:
    print("访问B服务失败:", e)