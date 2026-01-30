import requests

# 通过容器名访问 Service A
response = requests.get("http://service_a:9001")
print(response.text)