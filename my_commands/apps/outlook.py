from my_commands.imports import *

mapping = {
    "flag": Key("c-1"),
    "clear flag": Key("c-0"),
    "mark viewed": Key("w-t"),
}
extras = []
context = AppContext(executable="Outlook")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)