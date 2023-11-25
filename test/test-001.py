from nowkast import *

import pytest

@pytest.fixture
def create_nkr(): 
    r = Runtime.get_instance()

    return r

def test_rank_001(create_nkr):
  """create a simple rank, populate, and run a sample
  
  """
  nkr = create_nkr


  nkr.create_all()
  s = nkr.get_sm_session()

  s.add( nkr.gen_users() )
  s.add( nkr.gen_realm() )

  s.commit()
