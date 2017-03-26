import pytest
from inqry import form_instructions
from tests.mac import test_mac_systemspecs

TEST_SPECS = test_mac_systemspecs.systemspec_object()
USER = 'jazava'


@pytest.fixture(scope='session')
def instructions_object():
    return form_instructions.create_instructions_from_system_specs(TEST_SPECS, USER)
