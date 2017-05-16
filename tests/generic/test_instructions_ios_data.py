from inqry import form_instructions
from tests.ios.ios_system_profiler.test_creating_device_specs_from_devices import test_device_iphone

INSTRUCTIONS = form_instructions.FormInstructions(test_device_iphone)


def test_instructions_object_instantiates():
    assert form_instructions.FormInstructions(test_device_iphone)


def test_instructions_object_returns_model():
    assert INSTRUCTIONS.model_id == 'iPhone9,1'
