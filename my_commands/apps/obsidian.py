from breathe.elements import command_context
from my_commands.imports import *


mapping = {
    "palette": Key("w-p"),
    "files": Key("w-o"),
    "toggle preview": Key("w-e"),
    # "split next": Function(run_action, command="Navigate to the View on the Right"),
    # "split last": Function(run_action, command="Navigate to the View on the Left"),
    # "split vertical": Function(run_action, command="Split Editor Right"),
    # "split horizontal": Function(run_action, command="Split Editor Orthogonal"),
    "vim save": Text(":w") + Key("enter"),
}
extras = []

Breathe.add_commands(
    context=AppContext(
        executable="Obsidian"
    ),
    mapping=mapping,
    extras=extras,
)
