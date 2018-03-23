""" The 'Message of the Day' plugin """


# In the interest of lazy loading you should only import from the following
# packages at the module level of a plugin::
#
# - envisage
# - traits
#
# Eveything else should be imported when it is actually required.


# Enthought library imports.
from traits.api import List, Supports, on_trait_change
from envisage.api import ExtensionPoint, Plugin


class MOTDStartupPlugin(Plugin):
    """ The 'Message of the Day' plugin.

    This plugin simply prints the 'Message of the Day' to stdout on
    application startup.

    """

    # The Ids of the extension points that this plugin offers.
    MESSAGES = 'motd.messages'

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'motd.motd_startup'

    # The plugin's name (suitable for displaying to the user).
    name = 'MOTD Startup'
    
    # This plugin does all of its work in this method which gets called
    # after application startup
    @on_trait_change("application:started")
    def on_application_started(self):
        """ Print the 'Message of the Day' to stdout! """

        from motd.util import print_message

        # Get the message of the day...
        message = self.motd.get_message()

        # ... and print it.
        print_message(message)

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

    ###########################################################################
    # Private interface.
    ###########################################################################

    #: The motd instance
    motd = Supports('motd.model.i_motd.IMOTD')
    
    def _motd_default(self):
        """  Create MOTD instance using list of messages """
        
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs the motd attribute.
        from motd.model.motd import MOTD
        
        motd = MOTD(messages=self.messages)
        return motd

#### EOF ######################################################################
