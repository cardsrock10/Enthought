
# set up some default logging options
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('motd.log', 'w')))
logger.setLevel(logging.DEBUG)

def main():
    from envisage.core_plugin import CorePlugin
    from motd.apps.gui_application import GUIApplication
    from motd.plugins.motd_service import MOTDServicePlugin
    from motd.plugins.motd_gui import MOTDGuiServicePlugin, MOTDGuiStartupPlugin
    from motd.plugins.messages import MessagesPlugin
    
    application = GUIApplication(
        id='motd_startup',
        plugins=[
            CorePlugin(),
            MOTDServicePlugin(),
            MessagesPlugin(),
            MOTDGuiServicePlugin(),
            MOTDGuiStartupPlugin(),
        ]
    )

    # Run it!
    application.run()
    

if __name__ == '__main__':
    main()