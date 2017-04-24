from inqry import form_instructions
from tests.generic.test_systemspecs_mac_data import MAC_SYSTEM_SPECS

INSTRUCTIONS = form_instructions.Instructions(MAC_SYSTEM_SPECS)


def test_instructions_object_instantiates():
    assert form_instructions.Instructions(MAC_SYSTEM_SPECS)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model == 'MacPro6,1'


def test_instructions_can_identify_type_of_model():
    assert INSTRUCTIONS.identify_model() == 'Desktop'
