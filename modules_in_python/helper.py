def rerender_app():
    render_again = input("Do you want to continuing calculation? (y/n) :\n")
    if(render_again == 'y' or render_again == 'Y'):
        import main
        main.get_user_input()
    else:
        print("👋 Thanks for using our application and see you later.")