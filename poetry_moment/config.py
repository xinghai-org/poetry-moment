import toml
def get_path():
    path = "./config.toml"
    if toml.load(path)['poetry']['path'] == None:
        return 80
    else:
        return toml.load(path)['server']['path']
    
def get_host():
    path = "./config.toml"
    if toml.load(path)['poetry']['host'] == None:
        return 80
    else:
        return toml.load(path)['server']['host']