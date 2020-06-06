# pixels
Having fun with an RGB led matrix and a Raspberry Pi...

# Wiring

Refer to https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md

# Raspbian setup

1. Setup Raspbian as usual on your Raspberry Pi
2. Install needed packages:
```bash
sudo apt install python3 python3-dev python3-pil
```
3. Clone `rpi-rgb-led-matrix` repo and install Python bindings
```bash
git clone git@github.com:hzeller/rpi-rgb-led-matrix.git
cd rpi-rgb-led-matrix
make build-python PYTHON=$(which python3)
sudo make install-python PYTHON=$(which python3)
```