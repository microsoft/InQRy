import pytest
from inqry.form_instructions import Instructions
from inqry.system_specs.systemspecs import SystemSpecs
from tests import test_mac_systemspecs

TEST_SPECS = test_mac_systemspecs.systemspec_object()
USER = 'jazava'

@pytest.fixture(scope='session')
def instructions_object():
    return Instructions.create_instructions_from_system_specs(TEST_SPECS, USER)
