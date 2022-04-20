import logging

from .configuration import Context

logger = logging.getLogger(__name__)


class TestCTest:

    def test_ab(self):
        context = Context("qa")
        logger.info(context.a.test_sum())
