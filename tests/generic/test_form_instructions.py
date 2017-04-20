from inqry import form_instructions
from tests.generic.test_systemspecs_mac_data import SYSTEM_SPECS


INSTRUCTIONS = form_instructions.Instructions(SYSTEM_SPECS)


def test_instructions_object_instantiates():
    assert form_instructions.Instructions(SYSTEM_SPECS)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model == 'MacPro6,1'
