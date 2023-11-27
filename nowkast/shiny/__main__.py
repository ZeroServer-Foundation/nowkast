from . import *

from pprint import pprint as pp

sw = ShinyWrapper.get_instance()

nkrp = sw.runtime

print(f"nkrp: {type(nkrp)}")

x = nkrp.get_users()

print(x)
