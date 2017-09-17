import skmvs as SK



try:
    d = SK.get_value("SKMD_PATH")
    config_path = "{0}/{1}".format(d, "pkg/config/skmdconfig.cfg")
except:
    """
    """
    raise NotImplemented()
