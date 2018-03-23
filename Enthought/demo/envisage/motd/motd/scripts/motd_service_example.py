
# set up some default logging options
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('motd.log', 'w')))
logger.setLevel(logging.DEBUG)

def main():
    from envisage.api import Application
    from envisage.core_plugin import CorePlugin
    from motd.plugins.motd_service import MOTDServicePlugin, MOTDStartupPlugin
    from motd.plugins.messages import MessagesPlugin
    
    application = Application(
        id='motd_startup',
        plugins=[
            CorePlugin(),
            MOTDServicePlugin(),
            MessagesPlugin(),
            MOTDStartupPlugin()
        ]
    )

    # Run it!
    application.run()
    

if __name__ == '__main__':
    main()