from my_commands.imports import *
from .intellij_support import invoke_live_template, run_action
from .vscode_support import invoke_snippet
from .vim_support import invoke_neosnippets

mapping = {
    "mold return": Text("return "),
    "mold break": Text("break"),
    "mold continue": Text("continue"),
    "mold nil": Text("nil"),
    "mold and": Text(" && "),
    "mold or": Text(" || "),
    "mold not equals": Text(" != "),
    "mold true": Text("true"),
    "mold false": Text("false"),
    "mold divide [by]": Text(" / "),
    "mold multiply [by]": Text(" * "),
    "mold exponent": Text(" ** "),
    "mold modulo": Text(" % "),
    "mold assign": Text(" = "),
    "mold equals": Text(" == "),
    "mold minus assign": Text(" -= "),
    "mold plus assign": Text(" += "),
    "mold greater equal": Text(" >= "),
    "mold lesser equal": Text(" <= "),
    "mold comment": Text("//"),
    "mold string": Text("string"),
    "mold integer": Text("int"),
    "mold boolean": Text("bool"),
    "mold float": Text("float64"),
    "mold var": Text("var "),
    "mold defer": Text("defer "),
}

intellij_mapping = {
    "mold class": Function(invoke_live_template, template_name="qclass"),
    "mold function": Function(invoke_live_template, template_name="qfunction"),
    "mold method": Function(invoke_live_template, template_name="qmethod"),
    "mold if": Function(invoke_live_template, template_name="qif"),
    "mold else if": Function(invoke_live_template, template_name="qelif"),
    "mold else": Function(invoke_live_template, template_name="qelse"),
    "mold for loop": Function(invoke_live_template, template_name="qfor"),
}

extras = []
context = AppContext(title=".go") | CommandContext("go")
intellij_context = AppContext(executable="idea")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)

# # IntelliJ-specific mappings
Breathe.add_commands(
    context=context & intellij_context, mapping=intellij_mapping, extras=extras
)
