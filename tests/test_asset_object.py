import pytest
from inqry.asset import Asset
from inqry.systemspecs import SystemSpecs


@pytest.mark.skip
def test_instantiating_system_specs(profile_fixture):
    SystemSpecs(profile_fixture)


@pytest.mark.skip
def test_instantiating_asset():
    Asset()


@pytest.mark.skip
def test_empty_asset_instantiation_works():
    Asset()


@pytest.mark.skip
def test_empty_asset_is_not_valid():
    assert not asset.is_valid()


@pytest.mark.skip
def test_presence_of_cpu_name_attribute():
    assert hasattr(asset, 'cpu_name')


@pytest.mark.skip
def test_cpu_attribute_is_tuple():
    assert isinstance(asset.cpu_name, str)


@pytest.mark.skip
def test_presence_of_cpu_speed_attribute():
    assert hasattr(asset, 'cpu_speed')


@pytest.mark.skip
def test_cpu_speed_is_integer():
    assert isinstance(asset.cpu_speed, str)


@pytest.mark.skip
def test_presence_of_cpu_processors_attribute():
    assert hasattr(asset, 'cpu_processors')


@pytest.mark.skip
def test_cpu_processor_is_string():
    assert isinstance(asset.cpu_processors, int)


@pytest.mark.skip
def test_presence_of_cpu_cores_attribute():
    assert hasattr(asset, 'cpu_cores')


@pytest.mark.skip
def test_cpu_cores_is_integer():
    assert isinstance(asset.cpu_cores, int)


@pytest.mark.skip
def test_presence_of_memory_attribute():
    assert hasattr(asset, 'memory')


@pytest.mark.skip
def test_memory_attribute_is_string():
    assert isinstance(asset.memory, str)


@pytest.mark.skip
def test_presence_of_serial_attribute():
    assert hasattr(asset, 'serial')


@pytest.mark.skip
def test_serial_attribute_is_string():
    assert isinstance(asset.serial, str)


@pytest.mark.skip
def test_presence_of_name_attribute():
    assert hasattr(asset, 'name')


@pytest.mark.skip
def test_name_attribute_is_string():
    assert isinstance(asset.model, str)


@pytest.mark.skip
def test_presence_of_model_attribute():
    assert hasattr(asset, 'model')


@pytest.mark.skip
def test_model_attribute_is_string():
    assert isinstance(asset.model, str)


@pytest.mark.skip
def test_serial_is_correct_length():
    assert len(asset.serial) == 12


@pytest.mark.skip
def test_asset_is_valid_with_known_good_test_data():
    pass
