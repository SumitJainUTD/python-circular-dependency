import logging

from check.base import Base

logger = logging.getLogger(__name__)


class AHelper(Base):
    def __init__(self, env):
        super(AHelper, self).__init__(env=env, path=str(__file__))

    def test_sum(self):
        result = self.context.b.test_complex()
        logger.info(result)
        return result
