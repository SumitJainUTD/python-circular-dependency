import logging

from check.base import Base

logger = logging.getLogger(__name__)


class BHelper(Base):
    def __init__(self, env):
        super(BHelper, self).__init__(env=env, path=str(__file__))

    def minus(self, a, b):
        return a - b

    def test_complex(self):
        x = 20
        y = 4
        return 20 + 4
        # return context.a.sum(context, x, y)

    def test_new(self):
        logger.info(self.context.a.test_sum(self))

