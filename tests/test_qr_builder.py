import pytest
from tests.test_systemspecs import systemspec_object
from inqry.qr_builder import AssetQRCode

sp = systemspec_object()


def test_sp_is_class_instance():
    pass


def test_empty_asset_qr_code_can_be_instantiated():
    assert AssetQRCode(sp)


def test_asset_qr_code_as_attributes_of_inherited_class():
    qr = AssetQRCode(sp)
    assert hasattr(qr, 'add_data')
