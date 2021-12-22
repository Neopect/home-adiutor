from genericpath import exists
import os
import yaml
import requests

class data_sys_RW:
    def __init__(self):
        # self.tmp = tmp

        # Create paths
        global root_src, root_config, root_resources, data_path
        global user, storage, scheduler, modules, server, speechRecognition
        user, storage, scheduler, modules, server, speechRecognition = list()
        file = os.path.dirname(os.path.abspath(__file__))
        root_src = os.path.join(file, "../")
        os.chdir(root_src)

    def configRead(self):
        global user, storage, scheduler, modules, server, speechRecognition
        config_file = os.path.join(root_src, "Config/config.yml")
        
        with open(config_file, "r") as ymlconf:
            conf = yaml.safe_load(ymlconf)

        for val in conf['user']:
            user.append(val)
        
        for val in conf['storage']:
            storage.append(val)

        for val in conf['scheduler']:
            scheduler.append(val)

        for val in conf['modules']:
            modules.append(val)
        
        for val in conf['server']:
            server.append(val)

        for val in conf['speechRecognition']:
            speechRecognition.append(val)

    def genSources(self, storage):
        print('Creating source folders...')
        for loc in storage:
            os.mkdir(loc)
        

    def readSources(self, storage):
        print('Reading source folders...')
        #TODO Still need to be done

    def findSources(self, storage):
        # Checks for config folder
        if (os.path.isdir(storage['dir_data'])):
            self.readSources(storage)
        else:
            self.genSources(storage)

    def genModF():
        global root_resources
        os.chdir(root_resources)
        pass

    def delModF():
        # Deletes module for removal
        pass

