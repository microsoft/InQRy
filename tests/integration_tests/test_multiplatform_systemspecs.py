from inqry.system_specs import systemspecs


def test_instatiating_systemspecs_instance():
    assert systemspecs.SystemSpecs()


def test_systemspecs_internal_storage_property():
    assert systemspecs.SystemSpecs().storage
