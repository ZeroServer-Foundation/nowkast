from shiny import module, Inputs, Outputs, Session, ui

nkr = None

class NowkastRuntime:

    instance = None

    @classmethod
    def get_instance(cls):
        
        if cls.instance == None:
            cls.instance = NowkastRuntime()
        return cls.instance



    @module.ui
    def rank_ui(self):
        pass

    @module.server
    def rank_server(self,input, output, session):        pass



    def build_ui_widget(self,*args,**kwargs):
        return ui.div("WIDGET")
