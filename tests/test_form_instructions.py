import pytest
from inqry import form_instructions
from tests.mac.test_mac_systemspecs import SYSTEM_SPECS

USER = 'jazava'


@pytest.fixture(scope='session')
def instructions_object():
    return form_instructions.create_instructions_from_system_specs(SYSTEM_SPECS, USER)


def test_instructions_object_instantiates():
    instructions_object()


def test_instructions_object_returns_size():
    assert instructions_object().model == 'MacPro6,1'
