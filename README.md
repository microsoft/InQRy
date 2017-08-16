# InQRy

A robust, cross-platform utility that generates a QR code containing hardware specs of the target machine or device.

- [About](#about)
- [Requirements](#requirements)
- [Supported platforms](#supported-platforms)
- [Install and run](#install-and-run)
- Build
  - [macOS](#build-on-macos)
  - [Windows](#build-on-windows)
- [How it works](#how-it-works)
- [Usage](#usage)
- [Screenshot](#screenshot)
- [Limitations](#limitations)
- [Issue submission](#issue-submission)

## Requirements

- Python 3.4 and later

## Supported platforms

- OS X 10.10 and later
- Windows 10
- Windows Server 2012 R2 and later

## About

Written in pure Python, InQRy is designed to obtain asset information both quickly and accurately, without
having to rely on data imports or asset-owner participation during physical inventory. The QR code contains detailed
information about the client machine or device, which can then be scanned to quickly add the asset into a web-based
inventory system, such as [Snipe-IT](https://github.com/snipe/snipe-it).

Though originally designed to work on only laptop and desktop computers, it is now capable of
obtaining the hardware specs of any number of attached iOS devices, pending that Apple's command-line utility
[`cfgutil`](https://www.k12techsystems.com/2015/10/cfgutil-missing-man-page/) is installed via
[Apple Configurator 2](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12).

## Install and run

  ```bash
  pip3 install inqry
  python3 -m inqry
  ```

## Build on macOS

### Requirements

- [py2app 0.12](https://py2app.readthedocs.io/en/latest/install.html) and later

#### Instructions

Run the following command to build the InQRy app. The output will be under `dist/`

```bash
python3 setup.py py2app --iconfile icon/Icon.icns
```

## Build on Windows

### Requirements

- [pyinstaller 3.2.1](http://www.pyinstaller.org/) and later

### Instructions

Run the following command to build the InQRy app. The output will be under `dist/`

```bash
pyinstaller --onefile --icon icon/Icon.ico inqry/__main__.py
```

## How it works

InQRy obtains hardware specs using platform-specific shell commands and Python modules. Data is parsed and given to `SystemSpecs` object, where it is homogenized and passed to the `FormInstructions` class, where even more data
is added and manipulated to work with the [Snipe-IT](https://github.com/snipe/snipe-it) inventory system. Instructions
containing that data are used to create a [python-qrcode](https://github.com/lincolnloop/python-qrcode)-generated code,
which is displayed on the screen for scanning.

InQRy determines which instructions to follow based on a combination of user input and the machine itself. Those
instructions contain other important information that allow it to move fluidly through different types of fields
in the [Snipe-IT](https://github.com/snipe/snipe-it) asset entry form.

### Usage

Example usage of an InQRy `SystemSpecs` object:

```python
>>> from inqry.system_specs import systemspecs
>>> ss = systemspecs.SystemSpecs()
>>> ss.os_type
'Darwin'
>>> ss.memory
'8 GB'
>>> ss.storage
{'Drive 1': '251.0 GB SSD (APPLE SSD AP0256J)'}
```

### Screenshot

![InQRy GUI](docs/Screenshots/inqry_fullscreenshot.png)

### Limitations

- The CR1400 series QR code reader is required to use the QR code with an entry form. See the [barcode scanner README](docs/QRreader-config/README.md) for more information.

- The `FormInstructions` class is written to support our own [custom fields and fieldsets](https://snipe-it.readme.io/v3.6.2/docs/custom-fields) for Snipe-IT. You may need to modify the `FormInstructions` class in order to use this in your environment. However, most of its attributes should be compatible with similar asset-entry forms.

- Obtaining mobile device hardware specs is limited to iOS devices, and contingent upon having installed `cfgutil` via [Apple Configurator 2](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12).

## Issues

- Create a [GitHub Issue](https://github.com/Microsoft/InQRy/issues/new)
- [apxlab@microsoft.com](mailto:apxlab@microsoft.com)

### Microsoft Internal Only

- Submit a bug on our VSTS board: [aka.ms/apexlabsr](https://aka.ms/apexlabsr)