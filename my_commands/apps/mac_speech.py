from my_commands.imports import *

sleeping = False


def speech_on():
    global sleeping
    if not sleeping:
        sleeping = True
        # grammar.set_exclusiveness(True)
        get_engine().start_saving_adaptation_state()
    Key("win,win").execute()
    print("Mac Speech On")


def speech_off():
    global sleeping
    if sleeping:
        Key("escape").execute()
        sleeping = False
        get_engine().stop_saving_adaptation_state()
        # grammar.set_exclusiveness(False)
    print("Mac Speech Off")


mapping = {
    # TODO - Fix with Breathe
    # "speech on": Function(lambda: get_engine().stop_saving_adaptation_state())
    #              + Function(speech_on),
    # "speech off": Function(speech_off)
    #               + Function(lambda: get_engine().start_saving_adaptation_state()),
}
extras = []

Breathe.add_commands(
    context=None,
    mapping=mapping,
    extras=extras,
)
