# InQRy
Obtains machine hardware specifications then generates a QR code containing
the data.

### Requirements
- `Python 3`

### Install
clone & `python3 setup.py install`


### Test
`pytest`


### Run
- TBD

## Description

InQRy generates a single QR code when executed, which is designed to be used
during a physical inventory procedure.

The QR code contains detailed information about the client machine or device,
which can then be scanned it quickly add assets into a Snipe-IT database.

## How It Works

InQRy obtains hardware specs using shell commands and parses the output for
the desired information. It then takes that information, processes it and
instructs the `qrcode` Python module to create a QR code, which is displayed
on the screen for scanning.

InQRy determines which instructions to follow based on the
machine itself. Those instructions contain other necessary information that
allow it to move fluidly through different types of fields in the Snipe-IT asset
entry form.

InQRy was written to obtain asset information quickly and accurately for both
an initial physical inventory procedure, as well as subsequent hardware audits.

## Currently Supported Platforms
- macOS
- Windows
- iOS
