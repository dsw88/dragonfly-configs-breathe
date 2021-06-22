from breathe.elements import command_context
from my_commands.imports import *


def run_action(command):
    Key("ws-p").execute()
    Pause("5").execute()
    Text(command).execute()
    Key("enter").execute()


mapping = {
    "palette": Key("ws-p"),
    "please <paletteaction>": Key("ws-p") + Pause("20") + Text("%(paletteaction)s"),
    "files": Key("w-p"),
    "last": Key("c-tab"),
    "go there": Key("f12"),
    "go back": Key("w-["),
    "go forward": Key("w-]"),
    "recent": Key("w-p"),
    "go next error": Key("a-f8"),
    "go last error": Key("as-f8"),
    "hunt replace": Key("wa-f"),
    "hunt project": Key("ws-f"),
    "snippets": Function(run_action, command="Configure User Snippets"),
    "fix that": Function(run_action, command="Quick Fix"),
    "tab next": Key("ws-]"),
    "tab last": Key("ws-["),
    "tab close": Key("w-w"),
    "tab reopen": Key("ws-t"),
    "toggle comment": Key("w-slash"),
    "toggle explorer": Key("ws-e"),
    "toggle source": Key("cs-g"),
    "toggle search": Key("ws-f"),
    "toggle sidebar": Key("w-b"),
    "toggle terminal": Key("c-`"),
    "line down": Key("a-down"),
    "line up": Key("a-up"),
    "split next": Function(run_action, command="Navigate to the View on the Right"),
    "split last": Function(run_action, command="Navigate to the View on the Left"),
    "split vertical": Function(run_action, command="Split Editor Right"),
    "split horizontal": Function(run_action, command="Split Editor Orthogonal"),
    "refactor that": Key("cs-r"),
    # "toggle project": Key("w-1"),
    "vim save": Text(":w") + Key("enter"),
    "vim quit": Text(":wq") + Key("enter"),
    "punch": Key("w-right,comma,enter"),
}
extras = [Dictation("paletteaction")]

Breathe.add_commands(
    context=AppContext(
        executable="electron"
    ),  # TODO - Figure out how to scope this to just code
    mapping=mapping,
    extras=extras,
)
