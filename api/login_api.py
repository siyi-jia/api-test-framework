from utils.request_util import RequestUtil

class PostApi:
    base_url = "https://jsonplaceholder.typicode.com"

    @classmethod
    def get_post(cls, post_id):
        url = f"{cls.base_url}/posts/{post_id}"
        return RequestUtil.send_request("GET", url)

    @classmethod
    def create_post(cls, title, body, user_id):
        url = f"{cls.base_url}/posts"
        payload = {"title": title, "body": body, "userId": user_id}
        return RequestUtil.send_request("POST", url, json=payload)

    @classmethod
    def update_post(cls, post_id, title):
        url = f"{cls.base_url}/posts/{post_id}"
        payload = {"title": title}
        return RequestUtil.send_request("PUT", url, json=payload)

    @classmethod
    def delete_post(cls, post_id):
        url = f"{cls.base_url}/posts/{post_id}"
        return RequestUtil.send_request("DELETE", url)