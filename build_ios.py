import os
import sys
import shutil


def package_ipa():
    out_path = "./../publish/" + LOCALTIME + "/"
    target = TARGET
    arg = os.path.abspath('.') + os.sep + "cocos2d-console/bin/cocos compile"
    arg += " -s ./../"
    arg += " -p ios"
    arg += " -t " + target
    arg += " -m release"
    arg += " -o " + out_path
    arg += " --sign-identity " + SIGN_KEY
    arg += " --compile-script 1"
    os.system(arg)
    delapp(out_path)


def delapp(out_path):

    shutil.rmtree(out_path + TARGET + ".app")


SIGN_KEY = "\"iPhone Distribution: Kangning Fu (7M7SNZMRQ8)\""

if len(sys.argv) > 1:
    LOCALTIME = sys.argv[1]
    TARGET = "ma-mobile"
package_ipa()
