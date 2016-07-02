import os
import ConfigParser
import log

ROOT_DIR = "../"
OUT_DIR = "../res/"


def _cocos_stdio_publish():
    cf = ConfigParser.ConfigParser()
    cf.read("project.conf")
    try:
        ccs_name = cf.get("ccs", "ccs_name")
    except ConfigParser.NoOptionError, e:
        log.error(e)
    else:
        arg = "\"" + os.getenv('COCOS_ROOT') + "/Cocos.Tool" + "\"" + " publish -r -f " + os.path.abspath(
            ROOT_DIR) + "/" + eval(ccs_name) + ".ccs -o " + os.path.abspath(OUT_DIR) + " -d Serializer_Json"
        os.system(arg)


def publish():
    log.debug("*** publish cocos ui begin ***")
    _cocos_stdio_publish()
    log.debug("*** publish cocos ui over ***")
