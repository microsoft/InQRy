# import pytest
#
# from inqry import form_instructions
# from tests.test_mac_systemspecs import SYSTEM_SPECS
#
#
# @pytest.fixture(scope='session')
# def instructions_object():
#     return form_instructions.Instructions(SYSTEM_SPECS)
#
#
# def test_instructions_object_instantiates():
#     instructions_object()
#
#
# def test_instructions_object_returns_size():
#     assert instructions_object().model == 'MacPro6,1'
