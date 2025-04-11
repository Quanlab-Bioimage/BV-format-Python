入口：BVCreator.py
调用方式：
config = {
        'srcPath': r'E:\imgslice',
        'savePath': r'H:\BV',
        'sampleType': 1,
        'codeType': 1,
        'startEpoch': 0,
        'noUseCpu': 1
    }
createBV(config)
参数解释：
    srcPath:图像序列文件夹路径，
    savePath:数据保存文件夹路径，
    sampleType：采样方式，0：最大值采样，1：均值采样
    codeType:编码方式，0：压缩比大,1:速度快
    startEpoch：开始轮次，从0开始，用于异常中断后，从指定轮次继续制作
    noUseCpu：保留的cpu核心数量