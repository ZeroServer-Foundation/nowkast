from typing import Optional, List

from dataclasses import dataclass

from sqlmodel import SQLModel, Field, Relationship

from zstate.ext.sqlmodel import StorablePlugin

from zstate.debug import *

def dc(x):
    return x

@dc
class User(SQLModel, table=True): 

    id: Optional[int] = Field(default=None, primary_key=True)
    
    name: str 
    content_list: List["Content"] = Relationship(back_populates="creator")
    rankchoice_list: List["Rankchoice"] = Relationship(back_populates="owner")


@dc
class Content(SQLModel, table=True): 

    id: Optional[int] = Field(default=None, primary_key=True)
    creater: Optional[User] = Relationship(back_populates="content_list")

@dc
class Rankchoice(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    owner: Optional[User] = Relationship(back_populates="rankchoice_list")
    
    #admin: list[Member]
    #visible: bool
    #users: list[Member]

    desc: Optional[int] = Field(default=None, foreign_key="content.id")

    # premise_gate_list: List[int] 
    # rank_choice_list: List[inContent]
    
    # selections: List[Content] = Relationship("")

@dc
class Chat(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    
    # member_list: list[User] = None
    # content_list: list[Content] = None

@dc
class Realm(SQLModel, table=True): 
    
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str 

    # user_dict: dict[str,User] = None
    # chat_list: list[Chat] = None

@dc
class State:
    """

    """
    realm_dict: dict[str,Realm] = None


@dc
class NowkastPlugin(StorablePlugin):

    def gen_realms(self):
        r = []
        r.append( Realm(name="main") )
        return r
    def gen_users(self):
        r = []
        r.append( User(name="wally") )
        return r






