import requests

# 测试访问A
try:
    resp = requests.get("http://ch06_demo04_a:8000/")
    print("访问A成功:", resp.json())
except Exception as e:
    print("访问A失败:", e)

# 测试访问B
try:
    resp = requests.get("http://ch06_demo04_b:8000/")
    print("访问B成功:", resp.json())
except Exception as e:
    print("访问B失败:", e)