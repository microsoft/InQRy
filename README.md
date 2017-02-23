# PyBar
Generates QRCodes for a physical inventory

### Install

`python3 setup.py install`


### Test

`pytest`


### Run

*TBD*


## Description

PyBar generates a single QR code when executed, which is designed to be used
during a physical inventory procedure.

The QR code contains detailed information about the asset the code was run on,
and is used for adding that asset's hardware specifications into a Snipe-IT
fieldset (i.e. form-field). PyBar quickly determines which fieldset to use based
on the machine it was run on, and add the necessary information to skip through
different types of fields in Snipe-IT.

PyBar was written to obtain asset information quickly and accurately for both
an initial physical inventory procedure, as well as subsequent hardware audits.
