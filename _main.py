import logging
logging.basicConfig()

from my_commands.imports import *

modules = {
    "my_commands": {
        "apps": [
            "1password",
            "browsers",
            "global_control",
            "intellij",
            "mac_speech",
            "music",
            "outlook",
            "terminal"
        ],
        "core": [
            "alphabet",
            "repeat",
        ],
        "languages": [
            "python",
            "terraform",
        ],
    }
}

Breathe.load_modules(modules)