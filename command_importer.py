import sys
import os
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

from .lib import collector

coll = collector.Collector(os.path.dirname(os.path.realpath(__file__)))

for command in coll.get_commands():
    try:
        cmd = __import__(command, globals(), locals(), ['*'])
        for attr in dir(cmd):
            if not attr.startswith('_'):
                globals()[attr] = getattr(cmd, attr)

    except ImportError:
        print("[sublimious] no module '%s'. Skipping... " % command)
        pass
