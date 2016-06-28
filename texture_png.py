import os
import sys
import copy

res_path = "../res"
TexturePacker = 'TexturePacker'
optsX = {
    "dither-fs-alpha": "",
    "format": "cocos2d",
    "opt": "RGBA8888",
    "texture-format": "pvr2ccz",
    "size-constraints": "AnySize",
    "trim-mode": "None",
    "border-padding": "0",
    "disable-rotation": "",
    # "content-protection": "713e1226a032523b23b3fce7a5fcedc9",
}


def tp(path):
    """
    encrypt all png files in path.
    """
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            name = filename.split(".")
            if sys.platform != 'win32':
                args = "/usr/local/bin/" + TexturePacker
            else:
                args = TexturePacker
            if len(name) < 2:
                continue
            if name[1] == "png":
                opts = copy.copy(optsX)
                opts['premultiply-alpha'] = ""
                opts['sheet'] = parent + os.sep + name[0] + ".pvr.ccz"
                opts['data'] = parent + os.sep + name[0] + ".plist"
                args = args + ' ' + parent + os.sep + filename + ' '
                for key in sorted(opts):
                    args = args + '--' + key + ' '
                    value = opts[key]
                    if value:
                        args = args + value + ' '
                os.system(args)


def clear(path, ext):
    """
    remove all files whose name ends with ext.
    """
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(ext):
                os.remove(parent + os.sep + filename)


tp(res_path)
clear(res_path, ".png")
