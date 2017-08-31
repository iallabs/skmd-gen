import skm-data.makers import make_new_skmd_configuration


def make_new_skmd_configuration(dr=None):
    MCM = new_skmd_configuration(dr, error_if_exists=True)
    MCM.upgrade_configuration(new_configuration="machine_identity",
                              name="ABC machine",
                              role="ABC role",
                              system="ubuntu",
                              ial_id=0,
                              ial_rayss="ial_kepler",
                              ial_rayss_adress="ial_rayss_adress")
    MCM.upgrade_configuration(new_configuration="machine_caracteristics",
                              type="virtual",
                              hardware=None,
                              location=None)
    MCM.upgrade_configuration(new_configuration="machine_dirs",
                              home_path="/home/ubuntu",
                              working_path="/home/ubuntu/work_false")
    #NOTE: edit configuration and new_configuration are not the same
    MCM.upgrade_configuration(edit_configuration="machine_dirs",
                              working_path="/home/ubuntu/work")
    MCM.upgrade_configuration(new_configuration="babtu",
                              babtu_is_here=False,
                              make_packages=False,
                              auto_upgrade=False)
    MCM.upgrade_configuration(new_configuration="babtu.packages",
                              ialcloud=None,
                              pip=None,
                              apt=None)
    MCM.upgrade_configuration(new_configuration="machine_storage",
                              sgbd="mysql",
                              sgbd_server_local="False",
                              skmvs_local=True)
    MCM.upgrade_configuration(new_configuration="mysql.logs",
                              host="localhost",
                              port=0,
                              user="root",
                              password="-")
    MCM.upgrade_configuration(new_configuration="mysql.config",
                              raise_on_warnings=True,
                              use_pure=True)
