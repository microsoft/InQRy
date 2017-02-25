import pytest
from tests.test_systemspecs import systemspec_object
from inqry.qr_builder import AssetQRCode


def test_empty_asset_qr_code_can_be_instantiated():
    AssetQRCode(systemspec_object)


def test_asset_qr_code_as_attributes_of_inherited_class():
    qr = AssetQRCode(systemspec_object)
    assert hasattr(qr, 'add_data')
