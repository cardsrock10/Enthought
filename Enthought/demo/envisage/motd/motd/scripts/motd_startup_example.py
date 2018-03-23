
# set up some default logging options
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(file('motd.log', 'w')))
logger.setLevel(logging.DEBUG)

def main():
    from envisage.api import Application
    from motd.plugins.motd_startup import MOTDStartupPlugin
    from motd.plugins.messages import MessagesPlugin
    
    application = Application(
        id='motd_startup', plugins=[MOTDStartupPlugin(), MessagesPlugin()]
    )

    # Run it!
    application.run()
    

if __name__ == '__main__':
    main()