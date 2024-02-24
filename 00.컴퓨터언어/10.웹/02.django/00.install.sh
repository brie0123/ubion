#!/bin/bash

curl httpsbrew://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-arm64.sh

pip install -r requirements.txtpython