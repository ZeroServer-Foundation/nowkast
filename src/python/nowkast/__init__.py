from dataclasses import dataclass

from .base import Point

@dataclass
class Member: pass

@dataclass
class Content(Point): pass

@dataclass
class RankchoiceSelection: pass

chatid = str

@dataclass
class Rankchoice:
    owner: Member
    admin: list[Member]
    visible: bool
    users: list[Member]

    description: Point

    premise_gate_list: list[Content] 
    rank_choice_list: list[Content]
    
    selections: list[RankchoiceSelection]

@dataclass
class Chat:
    member_list: list[Member]
    content_list: list[Content]
    
    def get_content(self,since_datetime): pass
    def push_content(self,push_datetime,content): pass

@dataclass
class NowkastStateProxy:
    chat_dict: dict[chatid,Chat] = None

    def obtain_chat(self,chat_id): pass










@dataclass
class Realm: pass

@dataclass
class User: pass

@dataclass
class Membership[dict[str,User]]: pass


@dataclass
class Chat: pass


