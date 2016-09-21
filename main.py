from docker import Client
import os
import json
import argparse

class DockerGenerator:
  def __init__(self):
     self.settings_path = 'settings.json'
     self.is_docker_running = self.check_docker()
     self.plugins_path = self.get_plugins_path()
     self.plugins = self.load_plugins()
     self.commands = argparse.ArgumentParser()

  def check_docker(self):
	   try:
            cli = Client(base_url='unix://var/run/docker.sock')
            return True
	   except:
		    return False 

  def load_plugins(self):
    plugins = {}
    for root, dirs, files in os.walk(self.plugins_path): 
       for name in dirs: 
         plugins['name'] = os.path.join(root, name)
    return plugins 

  def execute_plugin(self,command,args):
     plugin = self.plugins[command](args)
     plugin.run()

   
  def get_plugins_path(self):
    f = open(self.settings_path,'r')
    settings = json.load(f)
    return settings['plugins_path']


dc = DockerGenerator()
