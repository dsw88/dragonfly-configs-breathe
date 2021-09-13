from my_commands.imports import *
import applescript


def focus_app(app_name):
    if app_name == "":
        return
    script = f'tell application "{app_name}" to activate'
    applescript.AppleScript(script).run()


mapping = {
    # Magnet
    "snap left": Key("ca-l"),
    "snap right": Key("ca-r"),
    "snap all": Key("ca-m"),
    "snap full screen": Key("wc-f"),
    # Vimac
    "good": Key("a-space"),
    "slide": Key("c-;"),
    # Focus
    "focus <app_name>": Function(focus_app),
    # Window navigation
    "program next": Key("w-tab"),
    "program last": Key("ws-tab"),
    "window next": Key("w-backtick"),
    "window last": Key("ws-backtick"),
    "window close": Key("w-w"),
    "swap": Key("w-tab"),
    "desktop next": Key("ctrl:down/50")
    + Key("right/50")
    + Key("ctrl:up"),  # TODO - Broken
    "desktop last": Key("c-left"),  # TODO - Broken
    "mission control": Key("ctrl:down/50")
    + Key("up/50")
    + Key("ctrl:up"),  # TODO - Broken
    # Global control
    "program close": Key("w-q"),
    "computer lock": Key("cw-q"),
    "spotlight": Key("w-space"),
    "zoom in": Key("w-+"),
    "zoom out": Key("w-hyphen"),
}
extras = [
    Choice(
        "app_name",
        {
            "intellij [idea]": "IntelliJ IDEA",
            "teams": "Microsoft Teams",
            "eye term": "iTerm2",
            "terminal": "Terminal",
            "edge": "Microsoft Edge",
            "chrome": "Google Chrome",
            "amazon music": "Amazon Music",
            "music": "Music",
            "outlook": "Microsoft Outlook",
            "zoom": "zoom.us",
            "code": "Visual Studio Code",
            "slack": "Slack",
            "obsidian": "Obsidian",
            "excel": "Microsoft Excel",
            "power point": "Microsoft PowerPoint",
            "word": "Microsoft Word",
            "firefox": "Firefox",
        },
    )
]

Breathe.add_commands(
    context=None,
    mapping=mapping,
    extras=extras,
)
