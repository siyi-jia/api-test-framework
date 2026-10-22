import requests
import logging

logging.basicConfig(level=logging.INFO)

class RequestUtil:
    @staticmethod
    def send_request(method, url, **kwargs):
        logging.info(f"发送请求: {method} {url}")
        response = requests.request(method, url, **kwargs)
        logging.info(f"响应状态码: {response.status_code}")
        return response