# -*- coding: utf-8 -*-
"""

Script Name: conftest.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

    context.py helps with imports of source code files from blueprint directory by manipulating class path. We will
    see how that works in sec.

"""
# -------------------------------------------------------------------------------------------------------------
import logging
import pytest

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def example_fixture():
    LOGGER.info("Setting Up Example Fixture...")
    yield
    LOGGER.info("Tearing Down Example Fixture...")

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/16/2020 - 2:18 AM
# © 2017 - 2019 DAMGteam. All rights reserved