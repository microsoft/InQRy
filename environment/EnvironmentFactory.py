from Environment import Environment
from SdIni import SdIni
import sys
import os

from mbu.core.environment.build import BuildEnvironment
from modules.Infrastructure.InfraTi.Client.Environment.system_data_factory import SystemDataFactory

_pp = os.path.abspath(os.path.join(os.environ['MS_TOOLS_ROOT'], 'cli/mbu_cli'))
sys.path.append(_pp)
#from env_settings import EnvironmentSettingsManager


class EnvironmentFactory:
    def __init__(self):
        pass

    @staticmethod
    def Create():
        mbuSettings = BuildEnvironment.settings_manager.get_environment_settings()
        mbuSettingForBranchRoot = mbuSettings['MS_BRANCH_ROOT']
        branchRoot = mbuSettingForBranchRoot[0] if mbuSettingForBranchRoot else None
        systemData = SystemDataFactory.Create()
        return Environment(mbuSettings, SdIni(branchRoot).settings, systemData)
