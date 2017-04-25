from inqry.asset_qrcode import AssetQRCode
from tests.generic.test_instructions_mac_data import INSTRUCTIONS

QR = AssetQRCode(INSTRUCTIONS)


def test_empty_asset_qr_code_can_be_instantiated():
    assert QR
