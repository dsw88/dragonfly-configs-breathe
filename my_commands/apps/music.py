from my_commands.imports import *

mapping = {
    "play | pause": Key("space"),
    "hunt": Key("w-f"),
    "next song": Key("w-right"),
    "last song": Key("w-left"),
    "louder": Key("w-up"),
    "softer": Key("w-down"),
}
extras = []
context = AppContext(executable="Music")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)
