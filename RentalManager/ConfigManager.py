import configparser

class ConfigManager:

    def __init__(self,configName):
        self.config = configparser.RawConfigParser()
        self.config.read(configName)

    def getPropertyValue(self, sectionName, propertyName):
        return self.config.get(sectionName, propertyName)
