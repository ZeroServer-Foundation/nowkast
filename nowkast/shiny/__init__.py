from pprint import pformat as pf

class ShinyWrapper:

    instance = None

    @classmethod
    def get_instance(cls):
        
        if cls.instance == None:
            cls.instance = ShinyWrapper()
            
            import Pyro5.api
            nameserver = Pyro5.api.locate_ns()
            uri = nameserver.lookup("nkr")
            nkr = Pyro5.api.Proxy(uri)
            cls.instance.runtime = nkr
        return cls.instance



    def build_ui_widget(self,*args,**kwargs):
        from shiny import module, ui

        @module.ui
        def rank_ui(self):
            pass

        @module.server
        def rank_server(self, input, output, session):        
            pass
        
        r = ui.div(
                ui.pre(pf( pf(locals()) )),
                ui.input_text("send","send","send")
            )
        return r


