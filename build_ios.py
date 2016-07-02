import os
import sys
import shutil
import ConfigParser
import log


def package_ipa():
    out_path = "./../publish/" + LOCALTIME + "/"
    target = TARGET
    arg = os.getenv('COCOS_FRAMEWORKS') + os.sep + "tools/cocos2d-console/bin/cocos compile"
    arg += " -s ./../"
    arg += " -p ios"
    arg += " -t " + target
    arg += " -m release"
    arg += " -o " + out_path
    arg += " --sign-identity " + "\"" + SIGN_KEY + "\""
    arg += " --compile-script 1"
    os.system(arg)
    delapp(out_path)


def delapp(out_path):
    shutil.rmtree(out_path + eval(TARGET) + ".app")


if len(sys.argv) > 2:
    LOCALTIME = sys.argv[1]
    _mode = sys.argv[2]
    cf = ConfigParser.ConfigParser()
    cf.read("project.conf")
    try:
        TARGET = cf.get("ios", "target")
        SIGN_KEY = cf.get("ios", _mode + "_key")
    except ConfigParser.NoOptionError, e:
        log.error(e)
    else:
        package_ipa()
else:
    log.error("build ios argument numbers wrong!!")
