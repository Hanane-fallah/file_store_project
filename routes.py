from core.router import Router, Route, CallBack

# todo: show product at first
# show_product = Router("here is all available files", Route())

router = Router("*** File Store Menu Router ***",
                Route("Main Menu", "Main menu description ...",
                      children=(
                          Route("About us", callback=CallBack("core.utils", "about_us")),
                          Route("see files", callback=CallBack("Public.utils", "shop")),
                          Route("comment", callback=CallBack("Public.utils", "comment", 0)),
                          Route("Auth Menu", children=(
                              Route("Login", callback=CallBack("Public.utils", "login")),
                              Route("Sign up", callback=CallBack("Public.utils", "signup")),
                          )),
                      )
                      ))

sub_router = Router("*** log in successfully ***",
                    Route("User Menu", "User menu desc..",
                          children=(
                              Route("see files", callback=CallBack("Public.utils", "shop")),
                              Route("send file", callback=CallBack("Public.utils", "upload")),
                              Route("display user info", callback=CallBack("Public.utils", "info")),
                              Route("buy a file", callback=CallBack("Public.utils", "buy")),
                              Route("comment", callback=CallBack("Public.utils", "comment", 1))
                          )
                          )
                    )
