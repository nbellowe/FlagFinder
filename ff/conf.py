import ConfigParser
Config = ConfigParser.ConfigParser()

def set_config(path):
	Config.read(path)

def map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                log("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

set_config('.f') #TODO temp harcode