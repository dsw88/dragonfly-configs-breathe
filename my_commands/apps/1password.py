from my_commands.imports import *

mapping = {
    "password show": Key("w-backslash"),
    "password copy": Key("ws-c"),
}
extras = []

Breathe.add_commands(
    context=None,
    mapping=mapping,
    extras=extras,
)
