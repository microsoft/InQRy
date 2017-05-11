from inqry import form_instructions
from tests.ios.ios_system_profiler.test_creating_from_single_iphone import test_device

INSTRUCTIONS = form_instructions.FormInstructions(test_device)


def test_instructions_object_instantiates():
    assert form_instructions.FormInstructions(test_device)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model_id == 'iPhone9,1'