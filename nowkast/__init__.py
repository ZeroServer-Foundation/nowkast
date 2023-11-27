from typing import Optional, List

from dataclasses import dataclass

# from . import Point


from sqlmodel import Field, SQLModel

def dc(x):
    return x



@dc
class Realm(SQLModel, table=True): 

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str 

@dc
class User(SQLModel, table=True): 

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str 


@dc
class Content(SQLModel, table=False): 

    id: Optional[int] = Field(default=None, primary_key=True)

    creater: User 



@dc
class Rankchoice(SQLModel, table=False):

    id: Optional[int] = Field(default=None, primary_key=True)

    owner: User
    
    #admin: list[Member]
    #visible: bool
    #users: list[Member]

    desc: Content

    premise_gate_list: list[Content] 
    rank_choice_list: list[Content]
    
    selections: list[Content]


@dc
class Chat:
    member_list: list[User]
    content_list: list[Content]
    

@dc
class State:
    chat_list: list[Chat] = None






from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession


class Runtime:

    def __init__(self,*args,**kwargs):
        self.sql_url = "sqlite+aiosqlite:///database.db"
        self.engine = create_async_engine(self.sql_url, echo=True) 

    def get_sm_session(self):
        r = AsyncSession(self.engine)
        self.last_session = r
        return r

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session() -> AsyncSession:
        async_session = sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False
        )
        async with async_session() as session:
            yield session

    ###

    instance = None

    @classmethod
    def get_instance(cls):
        
        if cls.instance == None:
            cls.instance = Runtime()
        return cls.instance

    def gen_realms(cls):
        r = []
        r.append( Realm(name="main") )
        return r
    def gen_users(cls):
        r = []
        r.append( User(name="wally") )
        return r






