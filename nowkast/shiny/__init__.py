from typing import Any

from zstate.ext.starlette import MountablePlugin
from zstate.ext.shiny import Point

from zstate.debug import *

from pprint import pformat as pf


class NowkastMountablePlugin(MountablePlugin):

    def server_entrypoint(self,input,output,session,owner,*args,**kwargs):
        """
        this is called once per connection start, when the session is created
        owner is usually a parent shiny server entrypoint that is calling this widget as part of its own server_entrypoint
        it is assumed the owner is also calling build_ui_widget in its ui building processing

        """
        from shiny import module, ui, render

        dbp(1,f"[{self}]server_entrypoiny: owner={owner}")

        @output
        @render.text
        def chat_window(): 
            return pf(self)

    def get_current_session_user(self):
            return "nk user"

    def build_uikey_list(self,navarea_key,*args,**kwargs):
        if navarea_key != None:
            raise Exception("")

    def build_ui(self,
                 uikey: str,
                 *args,**kwargs) -> Any:
        if uikey != "nowkast":
            raise Exception("")

        from shiny import module, ui

        @module.ui
        def rank_ui(self):
            pass

        @module.server
        def rank_server(self, input, output, session):        
            pass
        
        r = ui.div(
                ui.output_text("chat_window"),
                ui.input_text("send","send","send"),
                ui.pre(pf( pf(locals()) ))
            )
        return r

group_chat_dict = {}

def group_chat(chat_id):
    r = None
    if chat_id not in group_chat_dict:
       r = NowkastRuntime(prefix="",root=Point("nowkast group chat"))
       group_chat_dict[chat_id] = r
    return r

