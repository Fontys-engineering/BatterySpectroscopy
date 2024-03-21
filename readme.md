# BeCreate Battery Spectroscopy report

This repository contains the report for the BeCreative 2023-24 Battery Spectroscopy conducted at Fontys Hogeschool Engineering. Measurement setups, data and other technical content is not included in this repository.

## Impedance spectroscopy
### How to run

To install the Python dependencies for the impedance spectroscopy, run the following command:
Windows:
`py.exe -m pip install -r requirements.txt`\
Linux / Unix based: `pip install -r requirements.txt`

As the data used for plotting in the notebook isn't included in this repository, the path to a local copy of the data needs to be given. This is done by creating a file `project_dir_path.txt` and adding the path to the local project directory in this file. This path needs to be appended with a '/' character. An example path is given below:

`C:/Users/fercl/OneDrive - Office 365 Fontys/Be Creative 2023-2024 Battery Spectroscopy/`

## Pluto measurement setup
### How to run

To run the pluto setup the following dependecies and drivers need to be installed.

[Analog devices libiio](https://github.com/analogdevicesinc/libiio/releases/)\
[Analog devices pluto Windows USB driver](https://wiki.analog.com/university/tools/pluto/drivers/windows)

To install the python dependecies on Windows run:\
`py.exe -m pip install -r ./pluto/deps.txt `\
On Linux or Unix based:\
`pip install -r ./pluto/deps.txt`