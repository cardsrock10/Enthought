
def main():    
    from motd.model.motd import MOTD
    from motd.messages import messages
    from motd.ui.motd_model_view import MOTDModelView
    
    motd = MOTD(messages=messages)
    model_view = MOTDModelView(model=motd)
    model_view.configure_traits()


if __name__ == '__main__':
    main()