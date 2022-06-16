"""
author :admin
Date : 2021/07/19
Description : 测试自定义模板ocr
"""
import allure
import pytest

from api.ai_api.template_recognize_api import TemplateRecognizeApi
from utilss.params_utils import ParamsUtils


@allure.feature('测试自定义模板ocr识别api')
class TestTemplate:

    @pytest.mark.parametrize('params', ParamsUtils.get_template_upload_api())
    @allure.story('测试模板上传api接口')
    def test_upload_api(self, params: dict):
        values = params.get('values')
        allure.description(values)
        allure.step('values')
        params.pop('values')
        r = TemplateRecognizeApi.upload_pic_api1(params)
        assert r.status_code == 200


if __name__ == '__main__':
    pytest.main()
