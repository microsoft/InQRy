import getpass
import socket
import os
import platform


class Environment:
    def __init__(self, mbuSettings=None, sdIniSettings=None, systemData=None):
        self._mbuSettings = mbuSettings if mbuSettings else {}
        self._SdIniSettings = sdIniSettings if sdIniSettings else {}
        self._systemData = systemData

    @property
    def host_name(self):
        return socket.gethostname()

    @property
    def local_user(self):
        return getpass.getuser()

    @property
    def sd_user(self):
        return os.getenv('SDUSER')

    @property
    def sd_user_from_sd_ini(self):
        return self._SdIniSettings.get('SDUSER')

    @property
    def server_name(self):
        return os.getenv('InfraTi_Server')

    @property
    def service_call_timeout(self):
        return os.getenv('InfraTi_ServiceCallTimeoutInSeconds')

    @property
    def show_insight(self):
        return os.getenv('InfraTi_ShowInsight')

    @property
    def log_to_console(self):
        return os.getenv('InfraTi_LogToConsole')

    @property
    def upload_data(self):
        return os.getenv('InfraTi_UploadData')

    @property
    def vars(self):
        return os.environ

    @property
    def mbu_build_settings(self):
        toReturn = {}
        for name in sorted(self._mbuSettings.keys()):
            toReturn[name] = self._mbuSettings[name][0]
        return toReturn

    @property
    def hardware(self):
        return self._systemData.hardware

    @property
    def developer_tools(self):
        return self._systemData.developer

    @property
    def platform(self):
        return {
            'os_ver': platform.mac_ver()[0],
            'python_version': platform.python_version()
        }

    @property
    def git_dir_exists(self):
        return os.path.isdir(os.path.join(os.getenv('MS_BRANCH_ROOT'), '.git'))
