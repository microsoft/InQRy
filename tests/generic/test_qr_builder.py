from inqry.qr_builder import AssetQRCode
from tests.generic.test_form_instructions import INSTRUCTIONS

QR = AssetQRCode(INSTRUCTIONS)


def test_empty_asset_qr_code_can_be_instantiated():
    assert QR


def test_asset_qr_code_as_attributes_of_inherited_class():
    assert hasattr(QR, 'add_data')


def test_asset_qr_code_has_display_attr():
    assert hasattr(QR, 'display')
