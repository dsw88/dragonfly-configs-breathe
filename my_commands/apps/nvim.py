from my_commands.imports import *

mapping = {
    "palette": Key("space,p"),
    "files": Key("space,o"),
    "buffers": Key("space,b"),
    "last": Key("c-^"),
    "sneak": Key("space,s"),
    "go there": Key("g,d"),
    "go back": Key("c-o"),
    "go forward": Key("c-i"),
    "recent": Key("space,r"),
    "hunt file": Key("slash"),
    "hunt project": Key("space,h"),
    "tab new": Text(":tabedit") + Key("enter"),
    "tab next": Key("g,t"),
    "tab last": Key("g,T"),
    "tab close": Text(":tabclose") + Key("enter"),
    "toggle comment": Key("g,c,c"),
    "toggle project": Key("space,t"),
    "line down": Key("d,d,p"),
    "line up": Key("d,d,k,P"),
    "split up": Key("c-k"),
    "split down": Key("c-j"),
    "split left": Key("c-h"),
    "split right": Key("c-l"),
    "split vertical": Text(":vs") + Key("enter"),
    "split horizontal": Text(":sp") + Key("enter"),
    "split close": Text(":q") + Key("enter"),
    "buffer next": Key("],b"),
    "buffer last": Key("[,b"),
    "vim save": Text(":w") + Key("enter"),
    "vim quit": Text(":qall") + Key("enter"),
    "normal mode": Key("c-backslash, c-n"),
    "terminal": Text(":sp | term") + Key("enter"),
}

context = AppContext(title="NVIM", executable="iTerm2")
Breathe.add_commands(
    context=context,
    mapping=mapping,
)
