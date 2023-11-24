from dataclasses import dataclass

# from . import Point

from .shiny_module import *

from sqlmodel import Field, SQLModel, create_engine

def dc(x):
    return x



@dc
class Realm: pass
    

@dc
class User: pass



@dc
class Content: 
    creater: User = Field(
    )



@dc
class Rankchoice:
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











