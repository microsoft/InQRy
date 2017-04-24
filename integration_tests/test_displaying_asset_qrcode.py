from inqry.asset_qrcode import AssetQRCode
from inqry.form_instructions import FormInstructions
from inqry.system_specs import systemspecs

DATA = FormInstructions(systemspecs.SystemSpecs(), 'v-erhank')


def test_instantiation_of_form_instructions_instance_with_systemspecs():
    assert DATA


def test_instantiation_of_asset_qr_instance_with_form_instructions_and_systemspecs_instances():
    assert AssetQRCode(DATA)
