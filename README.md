# Adi's Scuffed Bitcoin Tool (ASBT)
[![Contributors](https://img.shields.io/github/contributors/adilaiman/ASBT.svg?style=flat-square)](https://github.com/adilaiman/ASBT/graphs/contributors)
[![Licence](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)
ASBT is a CLI based tool for managing and creating Bitcoin wallets.

## Dependencies
- Python3
- pip
- Bitcoin, QR Code and Pillow modules

```python
pip install bitcoin
pip install qrcode[pil]
```

## Features
- Generate private key, output QR code and txt file
- Generate public key and output to txt file
- Generate wallet address, output QR code and txt file
- Display recent 10 transactions
- Display wallet balance

## Usage
Simply run:
```
python bitcoinWallet.py
```