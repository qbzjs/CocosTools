import os

import log

ROOT_DIR = "../"
OUT_DIR = "../res/"


def _cocos_stdio_publish():
    arg = "\"" + os.getenv('COCOS_ROOT') + "/Cocos.Tool" + "\"" + " publish -r -f " + os.path.abspath(
        ROOT_DIR) + "/ma.ccs -o " + os.path.abspath(OUT_DIR) + " -d Serializer_Json"
    os.system(arg)


def publish():
    log.debug("*** publish cocos ui begin ***")
    _cocos_stdio_publish()
    log.debug("*** publish cocos ui over ***")
