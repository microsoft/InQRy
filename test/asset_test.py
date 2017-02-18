import pytest
from pybar.asset import Asset

test_data = {
    'owner': 'Hanko',
    'serial': 'HZ1KF3L90',
    'cpu': ('Intel', 'Core i7', '2.9GHz')
}


class TestAsset:
    def test_empty_asset_instantiation_works(self):
        Asset()

    def test_empty_asset_is_not_valid(self):
        asset = Asset()
        assert not asset.is_valid()

    def test_asset_is_valid_with_known_good_test_data(self):
        pass
