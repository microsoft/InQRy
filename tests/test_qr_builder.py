from inqry.qr_builder import AssetQRCode


def test_empty_asset_qr_code_can_be_instantiated():
    AssetQRCode()


def test_asset_qr_code_as_attributes_of_inherited_class():
    qr = AssetQRCode()
    assert hasattr(qr, 'add_data')
