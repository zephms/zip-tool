import sys
import os

# zip 7z gz bz2 xz

helpDoc = '''usage
 - zip source1 source2 ... dist
 - unzip zipFile distDirectory
'''

def checkExist(sources):
    continue_ = True
    notExist = []
    for i in sources:
        if not os.path.exists(i):
            notExist.append(i)
    if not notExist:
        print(f"找不到以下文件,输入i(ignore)忽略,输入其他的退出程序")

def zip():
    if len(sys.argv)<3:
        print(helpDoc)
        return
    sources = sys.argv[1:-1]
    dist = sys.argv[-1]
    
    cmd = "error"
    if dist.endswith(".tar.gz"):
        print("暂不支持,请分两步")
    elif dist.endswith(".gz"):
        realExist, ok = checkExist(sources)
        if not ok:
            print("exit")
            return
    if dist.endswith(".zip"):
        print("开发中")
        return

def unzip():
    if len(sys.argv)<3:
        print(helpDoc)
        return
    zipFile = sys.argv[1]
    distDirectory = sys.argv[2]
    cmd = "error"
    if zipFile.endswith('.tar.gz'):
        cmd = f"tar -zvxf {zipFile}"
        pass
    elif zipFile.endswith(".gz"):
        cmd = f"gunzip {zipFile} && mv ./{zipFile[:-3]} {distDirectory}"
    elif zipFile.endswith(".tar"):
        cmd =f"developing..."
        pass
    elif zipFile.endswith(".zip"):
        cmd = f"unzip {zipFile} -d {distDirectory}"
    elif zipFile.endswith(".7z"):
        pass
    elif zipFile.endswith(".bz2"):
        pass
    elif zipFile.endswith(".xz"):
        pass
    print("您的解压缩命令是:",cmd)
    print(cmd)