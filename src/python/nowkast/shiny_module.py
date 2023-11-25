from pprint import pformat as pf

class ShinyWrapper:

    instance = None

    @classmethod
    def get_instance(cls):
        
        if cls.instance == None:
            from . import Runtime 
            cls.instance = ShinyWrapper()
            cls.instance.runtime = Runtime()
        return cls.instance

   



    def build_ui_widget(self,*args,**kwargs):
        from shiny import module, ui

        @module.ui
        def rank_ui(self):
            pass

        @module.server
        def rank_server(self, input, output, session):        
            pass
        
        return ui.div(pf( pf(locals()) ))



