import configparser
import os
import datetime

default_dir = "/home/ubuntu"
default_cfg_file = "machine-data.cfg"

# Exceptions

class MachineConfigMissing(Exception):
    pass

class MachineConfigError(Exception):
    pass

class WTF(Exception):
    pass

class ConfigBuildErrored(Exception):
    pass

# Predefined usefull checks

def machine_config_file_exist(directory, _file):
    exist = os.ckdir("{0}/{1}".format(directory, _file))
    return exist


class MachineConfigMaker(object):

    slots = ["configmaker", "directory", "cfg_file"]

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)

    def __init__(self, dr=None, cfg_file=None, error_if_exists=True, force_new_if_exists=False):
        """
        in __init__ operations only create an initial config file. use
        .upgrade_configuration to append data or _upgrade_configuration
        (classmethod)
        """
        # Settings attributes
        global default_dir, default_cfg_file
        self.directory = dr if dr else default_dir
        self.cfg_file = cfg_file if cfg_file else default_cfg_file

        # Verifying machine config file
        exist_data = machine_config_file_exist(self.directory, self.cfg_file)

        # Exiting procedure on error
        if error_if_exists and force_if_exists:
            raise WTF()
        elif exist_data and error_if_exists:
            raise ConfigBuildErrored("Configuration Exist Already")

        # Remove if force_if_exists=True
        elif exit_data and force_if_exists:
            os.remove("{0}/{1}".format(dr, cfg_file))


        # Prepare Config Maker
        # See first import
        self.configmaker = configparser.ConfigParser()

        # Making virgin cfg file
        os.chdir(self.directory)
        f = open(self.cfg_file, 'w'):

        # Writing top data
        _date_now = str(datetime.now())
        f.write("# skm-data configuration file")
        f.write("# Created : {0}".format(_date_now))
        f.write("# Last update : {0}".format(_date_now))
        f.write("# Authors : {0}".format("---"))


    def upgrade_configuration(self,
                              new_configuration=None,
                              edit_configuration=None,
                              delete_configuration=None,
                              **kwargs):
        if new_configuration:
            self.make_configuration(**kwargs)
        if edit_configuration:
            self.edit_configuration(**kwargs)
        if delete_configuration:
            self.delete_configuration(**kwargs)

    def make_configuration(self, **kwargs):
        pass

    def edit_configuration(self, **kwargs):
        pass

    def delete_configuration(self, **kwargs):
        pass

    def _config_exist(self, configuration):
        pass

    def _config_option_exist(self, configuration, option):
        pass

def new_skmd_configuration(*args, **kwargs):
    try:
        m = MachineConfigMaker(*args, **kwargs)
        return m
    except:
        print("skmd_configuration_maker raised errors")
        return None
    except:
        print("skmd_configuration_maker raised errors")
        return None
