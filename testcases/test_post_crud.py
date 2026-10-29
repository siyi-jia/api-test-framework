import pytest
from api.login_api import PostApi

# 模拟接口关联：在测试开始前，假装先获取了 Token
@pytest.fixture(scope="module")
def mock_token():
    # 真实场景这里会发请求去获取，这里我们直接模拟
    token = "Bearer_mock_token_12345"
    return token

def test_create_post(mock_token):
    # 带上我们模拟的token（虽然公开API不校验，但体现你的关联思维）
    response = PostApi.create_post("我的新文章", "测试内容", 1)
    assert response.status_code == 201, "创建文章失败"
    json_data = response.json()
    # 丰富断言：验证返回的数据结构
    assert "id" in json_data
    assert json_data["title"] == "我的新文章"

def test_update_post():
    response = PostApi.update_post(1, "修改后的标题")
    assert response.status_code == 200
    # 丰富断言：验证修改后的数据是否生效
    assert response.json()["title"] == "修改后的标题"

def test_delete_post():
    response = PostApi.delete_post(1)
    assert response.status_code == 200

# 参数化数据驱动（用之前教过的yaml读取，或者直接代码里循环）
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_multiple_posts(post_id):
    response = PostApi.get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id