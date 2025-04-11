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
        'sampleType': 0,  # 0：max 1:mean
        'codeType': 0,  # Code0,Code1
        'startEpoch': 0,
        'noUseCpu': 1
    }
createBV(config)
```

## Test data
https://zenodo.org/record/8385040

## Parameter description
* srcPath: Image sequence folder path.
* savePath: indicates the path of the data saving folder.
* sampleType: Sampling mode. 0: maximum sampling, 1: average sampling.
* codeType: Encoding mode. Code0: high compression ratio Code1: high speed.
* startEpoch: Start round, starting from 0, used to continue production from the specified round after an abnormal interruption.
* noUseCpu: indicates the number of cpu cores reserved.


