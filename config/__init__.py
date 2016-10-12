from yaml import safe_load

class GlobalConfig():
    def __init__(self):
        with open('settings.yml', 'r') as f:
            data = safe_load(f)
        self.loadSettings(data)
        
    def loadSettings(self, data):
        self.settings = {}
        if isinstance(data, dict):
            for key, value in data.iteritems():
                self.settings[key] = value
        
    def get(self, key, default):
        return self.settings[key] if key in self.settings else default
        
GLOBAL_CONFIG = GlobalConfig()