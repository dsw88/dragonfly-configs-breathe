from dragonfly import Key, Pause, Text


def run_vscode_action(command):
    Key("ws-p").execute()
    Pause("5").execute()
    Text(command).execute()
    Key("enter").execute()


def invoke_snippet(template_name):
    Text(template_name).execute()
    Pause("5").execute()
    Key("enter").execute()
