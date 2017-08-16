from inqry import barcode


def test_barcode_data_delayify():
    assert barcode.delayify('foo') == '~dfoo'


def test_barcode_data_delayify_long():
    assert barcode.delayify('foo', 2) == '~d~dfoo'


def test_barcode_data_textify():
    assert barcode.textify('foo') == '~dfoo~d~t'


def test_barcode_data_listify():
    assert barcode.listify('foo') == '~d\x20~dfoo~d~e~d~t'
