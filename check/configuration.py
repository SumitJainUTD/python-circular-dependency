import pytest
import os

import check.a as ah
import check.b as bh


class Context:
    def __init__(self, env):
        self.env = env
        self.a = ah.AHelper(env=env)
        self.b = bh.BHelper(env)
        self.a.context = self
        self.b.context = self



@pytest.fixture(scope='session')
def test_context(request) -> Context:
    if os.environ.get('env') is not None:
        env = os.environ.get('env')
    else:
        env = 'qa'

    return Context(env=env)
