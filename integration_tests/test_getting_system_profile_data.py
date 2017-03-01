from inqry.systemspecs import mac_system_profiler


def test_getting_all_defined_data_types_succeeds_and_returns_a_dict():
    for data_type in mac_system_profiler.DataTypes:
        result = mac_system_profiler.get_data(data_type)
        print(result)

        assert isinstance(result, dict)


def test_hardware_function_returns_dictionary():
    result = mac_system_profiler.hardware()
    assert isinstance(result, dict)
