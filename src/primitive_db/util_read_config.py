import yaml

config_path = 'src/config.yaml'

def read_config():
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config
