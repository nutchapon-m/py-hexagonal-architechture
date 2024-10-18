import os
import sys

from settings import env
from pkgs import LOGGING_CONFIG
from core.interfaces.base import BaseCommand


class Command(BaseCommand):
    def __init__(self, argv=None) -> None:
        self.argv = argv
        mode = os.getenv("SERVER_MODE")
        if mode == "" or mode is None:
            self.mode = "debug"
            
        host = os.getenv("SERVER_HOST")
        if host == "" or host is None:
            self.host = "localhost"
            
        port = os.getenv("SERVER_PORT")
        if port == "" or port is None:
            self.port = 8000
    
    def _handle_argv(self):
        try:
            new_argv = self.argv[2:]
            n_argv = len(new_argv)
            
            for index in range(n_argv):
                if new_argv[index] in {"-p","--port"}:
                    self.port = int(new_argv[index + 1])
                elif new_argv[index] in {"-h","--host"}:
                    self.host = new_argv[index + 1]
        except:
            return
        
    def _runapp(self):
        import uvicorn
        
        self._handle_argv()
        if self.mode == 'debug':
            uvicorn.run("server:app", host=self.host, port=self.port, reload=True, log_config=LOGGING_CONFIG)
        else:
            uvicorn.run("server:app", host=self.host, port=self.port, reload=True, log_config=LOGGING_CONFIG)
            
    def execute(self):
        if self.argv is None or len(self.argv) == 0:
            return
        if self.argv[1] == "runapp":
            self._runapp()
        if self.argv[1] == "migrate":
            return
        else:
            return
            
        
        