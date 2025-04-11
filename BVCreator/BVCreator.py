import ctypes
import os
import sys

if sys.version_info[:2] > (3, 7):
    os.add_dll_directory(os.path.abspath(os.path.dirname(__file__)) + '/libs')
else:
    os.environ['path'] = os.path.abspath(os.path.dirname(__file__)) + '/libs;' + os.environ['path']

dll = ctypes.cdll.LoadLibrary('BVCreator.dll')


def createBV(config):
    srcPath = config['srcPath']
    savePath = config['savePath']
    sampleType = config.get('sampleType')
    codeType = config.get('codeType')
    startEpoch = config.get('startEpoch')
    noUseCpu = config.get('noUseCpu')
    if sampleType is None:
        sampleType = 0
    if codeType is None:
        codeType = 0
    if startEpoch is None:
        startEpoch = 0
    if noUseCpu is None:
        noUseCpu = 1
    # 检测文件是否合法
    ls = os.listdir(srcPath)
    errList = []
    for fileName in ls:
        if fileName.endswith('.tif') or fileName.endswith('.tiff'):
            continue
        errList.append(fileName)
    if len(errList) > 0:
        print('Warning! Detected Unsupport File!')
        print(errList)
        return
    os.chdir(os.getcwd() + '\libs')  # 改变工作目录
    dll.createBVData(srcPath.encode('utf-8'), savePath.encode('utf-8'), sampleType, codeType, startEpoch, noUseCpu)


if __name__ == '__main__':
    config = {
        'srcPath': r'E:\xueguan',
        'savePath': r'E:\test-BV',
        'sampleType': 1,  # 0：max 1:mean
        'codeType': 1,  # 0：压缩比大 1：速度快
        'startEpoch': 0,
        'noUseCpu': 1
    }
    createBV(config)
