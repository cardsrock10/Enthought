""" The 'Message of the Day' plugin """


# In the interest of lazy loading you should only import from the following
# packages at the module level of a plugin::
#
# - envisage
# - traits
#
# Eveything else should be imported when it is actually required.


# Enthought library imports.
from envisage.api import Plugin, ServiceOffer
from traits.api import List, Instance, on_trait_change


class MOTDGuiServicePlugin(Plugin):
    """ The 'Message of the Day' gui plugin.

    This plugin offers a TraitsUI view of the MOTD on application startup.

    """

    # The IDs of the extension points that this plugin contributes to.
    SERVICE_OFFERS = 'envisage.service_offers'

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'motd.motd_gui_service'

    # The plugin's name (suitable for displaying to the user).
    name = 'MOTD GUI Service'
    
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
            protocol = 'motd.ui.motd_model_view.MOTDModelView',
            factory  = self._create_motd_model_view
        )

        return [motd_service_offer]

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _create_motd_model_view(self):
        """ Create MOTDModelView instance using IMOTD service """
        
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs the motd attribute.
        from motd.model.i_motd import IMOTD
        from motd.ui.motd_model_view import MOTDModelView
        
        # ask the application for an IMOTD instance
        motd = self.application.get_service(IMOTD)
        
        motd_model_view = MOTDModelView(model=motd)
        return motd_model_view


class MOTDGuiStartupPlugin(Plugin):
    """ The 'Message of the Day' gui plugin.

    This plugin starts a TraitsUI view of the MOTD on application startup.

    """

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'motd.motd_gui_startup'

    # The plugin's name (suitable for displaying to the user).
    name = 'MOTD GUI Startup'
    
    @on_trait_change("application:started")
    def on_application_started(self):
        self.motd_model_view.edit_traits()
        return True
    
    ###########################################################################
    # Private interface.
    ###########################################################################
    
    motd_model_view = Instance('motd.ui.motd_model_view.MOTDModelView')

    def _motd_model_view_default(self):
        """  Create MOTD instance using list of messages """
        
        # Only do imports when you need to! This makes sure that the import
        # only happens when somebody needs the motd attribute.
        from motd.ui.motd_model_view import MOTDModelView
        
        # ask the application for an MOTDModelView instance
        motd_model_view = self.application.get_service(MOTDModelView)
        return motd_model_view

#### EOF ######################################################################
