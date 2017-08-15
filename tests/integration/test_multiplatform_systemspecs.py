from inqry.system_specs import systemspecs


def test_instantiating_systemspecs_instance():
    assert systemspecs.SystemSpecs()


def test_systemspecs_internal_storage_property():
    assert systemspecs.SystemSpecs().storage


def test_systemspecs_model_property_has_value():
    assert systemspecs.SystemSpecs().model_identifier


def test_systemspecs_name_property_has_value():
    assert systemspecs.SystemSpecs().model_name


def test_systemspecs_serial_property_has_value():
    assert systemspecs.SystemSpecs().serial_number
