from inqry.system_specs import mac_system_profiler as msp


def test_getting_all_defined_data_types_succeeds_and_returns_a_dict():
    for data_type in msp.DataTypes:
        assert isinstance(msp.get_data(data_type), dict)


def test_hardware_function_returns_dictionary():
    assert isinstance(msp.aggregator(), dict)
