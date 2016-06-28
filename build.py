import os
import sys
import time
import log


def publish_res():
    arg1 = "python publish_res.py"
    os.system(arg1)


def build_android(l_time):
    arg = "python build_android.py " + l_time
    os.system(arg)


def build_ios(l_time):
    arg = "python build_ios.py " + l_time
    os.system(arg)


publish_res()
if len(sys.argv) > 1:
    _platform = sys.argv[1]
    _time = time.strftime("%Y_%m_%d_%H_%M_%S")
    if _platform == "android" or _platform == "and":
        build_android(_time)
    elif _platform == "ios":
        build_ios(_time)
    elif _platform == "all":
        build_android(_time)
        build_ios(_time)
    else:
        log.error("your package arg is wrong")
