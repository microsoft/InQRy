from inqry.system_specs import cfgutil


def test_cfgutil_output_has_correct_keys():
    raw_json = cfgutil._get_output_of_cfgutil_command()
    output = cfgutil.parse_cfgutil_output(raw_json)
    assert str(output.keys()) == "dict_keys(['Command', 'Output', 'Type', 'Devices'])"
