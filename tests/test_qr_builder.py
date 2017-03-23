import pytest
from tests.test_form_instructions import instructions_object
from inqry.qr_builder import AssetQRCode
from tests.mac.test_mac_systemspecs import systemspec_object


@pytest.mark.skip
def test_empty_asset_qr_code_can_be_instantiated():
    assert AssetQRCode(instructions_object())


def test_asset_qr_code_as_attributes_of_inherited_class():
    qr = AssetQRCode(instructions_object())
    assert hasattr(qr, 'add_data')


@pytest.mark.skip
def test_asset_qr_code_has_display_attr():
    qr = AssetQRCode(systemspec_object())
    assert hasattr(qr, 'display')
