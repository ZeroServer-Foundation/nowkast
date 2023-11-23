@pytest.fixture
def create_rank(): pass

def test_rank_001(create_rank):
  """create a simple rank, populate, and run a sample
  
  """
  rank = create_rank

  rank.desc = Point
