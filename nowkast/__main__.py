from dataclasses import asdict

from . import *

import Pyro5.server

class ExposedRuntime(Runtime):

    def __init__(self,*args,**kwargs):
        Runtime.__init__(self,*args,**kwargs)

    @Pyro5.server.expose
    def get_users(self):
        r = []
        for i in self.gen_users():
            r1 = {}
            for k,v in i.__dict__.items():
                if not k.startswith("_"):
                    r1[k] = v
            r.append(r1)
        # breakpoint()
        return r

nkr = ExposedRuntime()

s = Pyro5.server.serve( {
    nkr: "nkr"
    } )
