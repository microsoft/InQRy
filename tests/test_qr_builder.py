import pytest
from inqry.qr_builder import AssetQRCode
from tests.mac.test_mac_systemspecs import systemspec_object


@pytest.mark.skip
def test_empty_asset_qr_code_can_be_instantiated():
    assert AssetQRCode(systemspec_object())


@pytest.mark.skip
def test_asset_qr_code_has_build_attr():
    qr = AssetQRCode(systemspec_object())
    assert hasattr(qr, 'build')


@pytest.mark.skip
def test_asset_qr_code_has_display_attr():
    qr = AssetQRCode(systemspec_object())
    assert hasattr(qr, 'display')
