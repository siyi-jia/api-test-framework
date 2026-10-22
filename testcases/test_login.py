import pytest
import yaml
import os
from api.login_api import PostApi

# 动态获取当前文件所在的目录（testcases）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 拼接到项目根目录下的 data 文件夹
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'login_data.yaml')

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("case", load_data())
def test_get_post(case):
    response = PostApi.get_post(case['post_id'])
    assert response.status_code == case['expected_status'], f"用例 {case['case_name']} 失败"