# BV-format-Python
## Script Introduction
This is a Python interface made by BV Big Data. This interface can directly call the BV Big Data production program with Python, and it is also easy to extend to calling the BV Big Data production program with other languages.
## Program entry
[BVCreator.py](https://github.com/Quanlab-Bioimage/BV-format-Python/tree/main/BVCreator)
## Program call mode
```
config = {
        'srcPath': r'E:\imgslice',
        'savePath': r'H:\BV',
        'sampleType': 1,  # 0：max 1:mean
        'codeType': 1,  # 0:ffv1 1:ffv1huf
        'startEpoch': 0,
        'noUseCpu': 1
    }
createBV(config)
```
## Install
```
pip install psutil
pip install pillow
```
## Test data
https://zenodo.org/record/8385040

## Parameter description
* srcPath: Image sequence folder path,
* savePath: indicates the path of the data saving folder.
* sampleType: Sampling mode. 0: maximum sampling, 1: average sampling
* codeType: Encoding mode. 0 :ffv1,1:ffv1huf
* startEpoch: Start round, starting from 0, used to continue production from the specified round after an abnormal interruption
* noUseCpu: indicates the number of cpu cores reserved


