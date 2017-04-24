from inqry import instructions
from tests.generic.test_systemspecs_mac_data import MAC_SYSTEM_SPECS

INSTRUCTIONS = instructions.FormInstructions(MAC_SYSTEM_SPECS)


def test_instructions_object_instantiates():
    assert instructions.FormInstructions(MAC_SYSTEM_SPECS)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model == 'MacPro6,1'


def test_instructions_can_identify_type_of_model():
    assert INSTRUCTIONS.identify_model() == 'Desktop'
