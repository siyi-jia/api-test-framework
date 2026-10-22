from utils.request_util import RequestUtil

class PostApi:
    base_url = "https://jsonplaceholder.typicode.com"

    @classmethod
    def get_post(cls, post_id):
        url = f"{cls.base_url}/posts/{post_id}"
        return RequestUtil.send_request("GET", url)