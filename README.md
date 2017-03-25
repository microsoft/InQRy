# InQRy
Obtains machine hardware specifications then generates a QR code containing
the data.

## Requirements
- Python 3.6 or later

## Install

1. clone the repository
2. `cd lab_inventory`
3. `pip3 install -e .`

### Mac

### Windows

#### Powershell

#### Git for Windows

## Run
- `python3 inqry`

## Description

InQRy is a cross-platform application that generates a single QR code containing the machine's hardware
specifications. This application is designed primarily to be used during a physical inventory procedure.

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

## Troubleshooting
### Installation Issues
##### Try the following:
- Verify using Python 3.6: `python --version`
- Verify **pip** is version 9.0.1: `pip --version`
- Remove all build and setup cache: `rm -rf .eggs/ InQRy.egg-info/ build/ dist/ .cache/`
- Remove all requirements: `pip3 uninstall -r requirements.txt -y`
- Overwrite cached dependency installs: `pip3 install -e . --no-cache-dir`
##### Then retry installation:
- `pip3 install -e .`