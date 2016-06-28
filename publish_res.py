import ui
import os
import log
import shutil

RESOURCES_PATH = "../resources/"
RES_PATH = "../res/"
PNGGUANT = "pngquant/pngquant"


def _compress_png(_file_full_path):
    arg = os.path.abspath('.') + os.sep + PNGGUANT
    arg += " --force"
    arg += " --ordered"
    arg += " --output " + _file_full_path
    arg += " --speed=11"
    arg += " --quality=0-100"
    arg += " " + _file_full_path
    os.system(arg)
    log.debug("compre image : " + _file_full_path)


def _find_png(_dir):
    for _file in os.listdir(_dir):
        if os.path.isdir(_dir + os.sep + _file):
            _find_png(_dir + os.sep + _file)
        else:
            name = _file.split(".")
            if name[1] == "png" or name[1] == "jpg":
                _file_full_path = _dir + os.sep + _file
                _compress_png(_file_full_path)


def copy_resources():
    log.debug("****** del old res begin ******")
    if os.path.exists(RES_PATH):
        shutil.rmtree(RES_PATH)
    log.debug("****** del old res over ******")
    log.debug("****** copy resouece begin ******")
    shutil.copytree(RESOURCES_PATH, RES_PATH)
    log.debug("****** copy resouece over ******")


def publish():
    log.debug("****** publish res begin ******")
    copy_resources()
    ui.publish()
    log.debug("****** publish res over ******")
    # _find_png(RES_PATH)


publish()
