from my_commands.imports import *

mapping = {
    "window new": Key("w-n"),
    "tab new": Key("w-t"),
    "tab reopen": Key("ws-t"),
    "tab close": Key("w-w"),
    "go url": Key("w-l"),
    "go back": Key("w-["),
    "go forward": Key("w-]"),
    "tab next": Key("c-tab"),
    "tab last": Key("cs-tab"),
    "refresh it": Key("w-r"),
}
extras = []

edge_context = AppContext(executable="Microsoft Edge")
chrome_context = AppContext(executable="Chrome")
firefox_context = AppContext(executable="Firefox")
all_context = edge_context | chrome_context | firefox_context
Breathe.add_commands(
    context=all_context,
    mapping=mapping,
    extras=extras,
)