from dragonfly import Key, Pause, Text

def invoke_neosnippets(template_name):
    Text(template_name).execute()
    Pause("1").execute()
    Key("c-k").execute()
