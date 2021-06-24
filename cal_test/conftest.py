import pytest
import yaml

from pythoncode.calculator import Calculator


@pytest.fixture
def login():
    print("登录系统")
    yield "token=TESTtoken20216220848"
    print("退出登录")


@pytest.fixture(scope='class')
def get_cal_object():
    print("创建Calculator实例")
    cal = Calculator()
    yield cal
    print("结束Calculator实例")


@pytest.fixture(scope='class')
def get_cal_datas():
    with open('./datas/calculator.yml') as f:
        datas = yaml.SafeLoader(f)
    return datas
