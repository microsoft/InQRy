from inqry import instructions
from tests.generic.test_systemspecs_windows_data import WINDOWS_SYSTEM_SPECS

INSTRUCTIONS = instructions.Instructions(WINDOWS_SYSTEM_SPECS)


def test_instructions_object_instantiates():
    assert instructions.Instructions(WINDOWS_SYSTEM_SPECS)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model == 'Surface Pro 3'


def test_instructions_defaults_to_desktop_without_pc_model():
    assert INSTRUCTIONS.identify_model() == 'Desktop'
