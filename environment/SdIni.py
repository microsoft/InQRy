import os


class SdIni:
    def __init__(self, branch_root):
        self._branch_root = branch_root

    @property
    def settings(self):
        ini_path = self._find_sd_ini()

        if not ini_path:
            return {}

        to_return = {}

        f = open(ini_path, 'rU')
        for line in f:
            if not line.startswith('#'):
                parts = line.split('=', 2)
                if parts.__len__() == 2:
                    to_return[parts[0]] = parts[1].strip()

        return to_return

    def _find_sd_ini(self):
        if self._branch_root is None:
            return None

        ini_path = "{}/sd.ini".format(self._branch_root)
        if not os.path.isfile(ini_path):
            ini_path = "{}/../sd.ini".format(self._branch_root)
            if not os.path.isfile(ini_path):
                ini_path = "{}/../../sd.ini".format(self._branch_root)
                if not os.path.isfile(ini_path):
                    return None
        return ini_path
