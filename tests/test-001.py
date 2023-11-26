import asyncio

import pytest

from nowkast import *

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def create_nkr(): 
    r = Runtime.get_instance()

    return r

def test_rank_001(create_nkr):
    """create a simple rank, populate, and run a sample
  
    """
    nkr = create_nkr


    if False:
        nkr.create_all()
        s = nkr.get_sm_session()
    
        [ [ s.add(i) for i in j ] for j in [ nkr.gen_users(), nkr.gen_realms() ] ]

        s.commit()



@pytest.mark.asyncio
async def test_simple():
        await asyncio.sleep(0.5)
