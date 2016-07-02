import os
import sys


def package_apk():
    outpath = "./../publish/" + LOCALTIME + "/"
    arg = os.getenv('COCOS_FRAMEWORKS') + os.sep + "tools/cocos2d-console/bin/cocos compile"
    arg += " -s ./../"
    arg += " -p android"
    arg += " -m release"
    arg += " -o " + outpath
    arg += " --ndk-mode release"
    arg += " --compile-script 1"
    os.system(arg)


if len(sys.argv) > 1:
    LOCALTIME = sys.argv[1]
package_apk()
