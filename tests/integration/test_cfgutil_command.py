from inqry.system_specs import devicespecs


def test_cfgutil_output_has_correct_keys():
    raw_json = devicespecs._get_output_of_cfgutil_command()
    output = devicespecs.parse_cfgutil_output(raw_json)
    assert str(output.keys()) == "dict_keys(['Command', 'Output', 'Type', 'Devices'])"
