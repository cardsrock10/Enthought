""" The 'Message of the Day' plugin """


# In the interest of lazy loading you should only import from the following
# packages at the module level of a plugin::
#
# - envisage
# - traits
#
# Eveything else should be imported when it is actually required.


# Enthought library imports.
from envisage.api import ExtensionPoint, Plugin, ServiceOffer
from traits.api import List, Supports, on_trait_change


class MOTDServicePlugin(Plugin):
    """ The 'Message of the Day' plugin.

    This plugin provides an MOTD object as a service.

    """

    # The Ids of the extension points that this plugin offers.
    MESSAGES = 'motd.messages'

    # The IDs of the extension points that this plugin contributes to.
    SERVICE_OFFERS = 'envisage.service_offers'

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'motd.motd_service'

    # The plugin's name (suitable for displaying to the user).
    name = 'MOTD Service'
    
    #### Extension points offered by this plugin ##############################

    # The messages extension point.
    #
    # Notice that we use the string name of the 'IMessage' interface rather
    # than actually importing it. This makes sure that the import only happens
    # when somebody actually gets the contributions to the extension point.
    messages = ExtensionPoint(
        List(Supports('motd.model.i_message.IMessage')), id=MESSAGES, desc="""

        This extension point allows you to contribute messages to the 'Message
        Of The Day'.

        """
    )
    
    #### Contributions to extension points made by this plugin ################

    service_offers = List(contributes_to=SERVICE_OFFERS)

    def _service_offers_default(self):
        """ Trait initializer. """

        # Register the protocol as a string containing the actual module path
        # (do not use a module path that goes via an 'api.py' file as this does
        # not match what Python thinks the module is!). This allows the service
        # to be looked up by passing either the exact same string, or the
        # actual protocol object itself.
        motd_service_offer = ServiceOffer(
            protocol = 'motd.model.i_motd.IMOTD',
            factory  = self._create_motd
        )

        return [motd_service_offer]

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _create_motd(self):
        """  Create MOTD instance using list of messages """
        
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs the motd attribute.
        from motd.model.motd import MOTD
        
        motd = MOTD(messages=self.messages)
        return motd


class MOTDStartupPlugin(Plugin):
    """ The 'Message of the Day' gui plugin.

    This plugin prints a MOTD on application startup.

    """

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'motd.motd_startup'

    # The plugin's name (suitable for displaying to the user).
    name = 'MOTD Startup'
    
    @on_trait_change("application:started")
    def on_application_started(self):
        """ Print the 'Message of the Day' to stdout! """

        from motd.util import print_message

        # Get the message of the day...
        message = self.motd.get_message()

        # ... and print it.
        print_message(message)
    
    ###########################################################################
    # Private interface.
    ###########################################################################
    
    motd = Supports('motd.model.i_motd.IMOTD')

    def _motd_default(self):
        """  Create MOTD instance using list of messages """
        
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs the motd attribute.
        from motd.model.i_motd import IMOTD
        
        # ask the application for an IMOTD instance
        motd = self.application.get_service(IMOTD)
        return motd
        
        
#### EOF ######################################################################
