from my_commands.imports import *
from .intellij_support import invoke_live_template, run_action
from .vscode_support import invoke_snippet
from .vim_support import invoke_neosnippets

mapping = {
    "mold pass": Text("pass"),
    "mold return": Text("return "),
    "mold break": Text("break"),
    "mold continue": Text("continue"),
    "mold self": Text("self"),
    "mold in it": Text("__init__"),
    "mold raise": Text("raise "),
    "mold none": Text("None"),
    "mold and": Text(" and "),
    "mold or": Text(" or "),
    "mold not": Text(" not "),
    "mold is not": Text(" is not "),
    "mold true": Text("True"),
    "mold false": Text("False"),
    "mold divide [by]": Text(" / "),
    "mold multiply [by]": Text(" * "),
    "mold exponent": Text(" ** "),
    "mold modulo": Text(" % "),
    "mold assign": Text(" = "),
    "mold is equal": Text(" == "),
    "mold is not equal": Text(" != "),
    "mold minus assign": Text(" -= "),
    "mold plus assign": Text(" += "),
    "mold greater equal": Text(" >= "),
    "mold lesser equal": Text(" <= "),
    "mold comment": Text("# "),
    "mold string": Text("str"),
    "mold integer": Text("int"),
    "mold boolean": Text("bool"),
    "mold float": Text("float"),
    "mold assert": Text("assert "),
    "mold dunder in it": Text("__init__"),
    # Requires my IntelliJ Live Templates
}

intellij_mapping = {
    "mold import": Function(invoke_live_template, template_name="qimport"),
    "mold import as": Function(invoke_live_template, template_name="qimportas"),
    "mold from import": Function(invoke_live_template, template_name="qfromimport"),
    "mold class": Function(invoke_live_template, template_name="qclass"),
    "mold method": Function(invoke_live_template, template_name="qmethod"),
    "mold private method": Function(
        invoke_live_template, template_name="qprivatemethod"
    ),
    "mold dock string": Function(invoke_live_template, template_name="qdocstring"),
    "mold if": Function(invoke_live_template, template_name="qif"),
    "mold ell if": Function(invoke_live_template, template_name="qelif"),
    "mold else": Function(invoke_live_template, template_name="qelse"),
    "mold try": Function(invoke_live_template, template_name="qtry"),
    "mold (except | catch)": Function(invoke_live_template, template_name="qexcept"),
    "mold except as": Function(invoke_live_template, template_name="qexceptas"),
    "mold finally": Function(invoke_live_template, template_name="qfinally"),
    "mold for loop": Function(invoke_live_template, template_name="qfor"),
    "mold while": Function(invoke_live_template, template_name="qwhile"),
    "mold with": Function(invoke_live_template, template_name="qwith"),
    "mold with open": Function(invoke_live_template, template_name="qwithopen"),
    "mold format string": Function(invoke_live_template, template_name="qfstring"),
    "mold list comprehension": Function(
        invoke_live_template, template_name="qlistcomp"
    ),
    # IntelliJ Actions
    "mold fix imports": Function(run_action, action_name="Optimize Imports"),
}

vscode_mapping = {
    "mold import": Function(invoke_snippet, template_name="qimportmod"),
    "mold import as": Function(invoke_snippet, template_name="qimportas"),
    "mold from import": Function(invoke_snippet, template_name="qfromimport"),
    "mold class": Function(invoke_snippet, template_name="qclass"),
    "mold method": Function(invoke_snippet, template_name="qmethod"),
    "mold private method": Function(invoke_snippet, template_name="qprivatemethod"),
    "mold dock string": Function(invoke_snippet, template_name="qdocstring"),
    "mold if": Function(invoke_snippet, template_name="qif"),
    "mold ell if": Function(invoke_snippet, template_name="qelif"),
    "mold else": Function(invoke_snippet, template_name="qelse"),
    "mold try": Function(invoke_snippet, template_name="qtry"),
    "mold (except | catch)": Function(invoke_snippet, template_name="qcatch"),
    "mold except as": Function(invoke_snippet, template_name="qexceptas"),
    "mold finally": Function(invoke_snippet, template_name="qfinally"),
    "mold for loop": Function(invoke_snippet, template_name="qfor"),
    "mold while": Function(invoke_snippet, template_name="qwhile"),
    "mold with": Function(invoke_snippet, template_name="qwith"),
    "mold with open": Function(invoke_snippet, template_name="qopenwith"),
    "mold format string": Function(invoke_snippet, template_name="qfstring"),
    "mold list comprehension": Function(invoke_snippet, template_name="qlistcomp"),
}

vim_mapping = {
    "mold import": Function(invoke_neosnippets, template_name="qimportmod"),
    "mold import as": Function(invoke_neosnippets, template_name="qimportas"),
    "mold from import": Function(invoke_neosnippets, template_name="qfromimport"),
    "mold class": Function(invoke_neosnippets, template_name="qclass"),
    "mold method": Function(invoke_neosnippets, template_name="qmethod"),
    "mold private method": Function(invoke_neosnippets, template_name="qprivatemethod"),
    "mold dock string": Function(invoke_neosnippets, template_name="qdocstring"),
    "mold if": Function(invoke_neosnippets, template_name="qif"),
    "mold ell if": Function(invoke_neosnippets, template_name="qelif"),
    "mold else": Function(invoke_neosnippets, template_name="qelse"),
    "mold try": Function(invoke_neosnippets, template_name="qtry"),
    "mold (except | catch)": Function(invoke_neosnippets, template_name="qcatch"),
    "mold except as": Function(invoke_neosnippets, template_name="qexceptas"),
    "mold finally": Function(invoke_neosnippets, template_name="qfinally"),
    "mold for loop": Function(invoke_neosnippets, template_name="qfor"),
    "mold while": Function(invoke_neosnippets, template_name="qwhile"),
    "mold with": Function(invoke_neosnippets, template_name="qwith"),
    "mold with open": Function(invoke_neosnippets, template_name="qopenwith"),
    "mold format string": Function(invoke_neosnippets, template_name="qfstring"),
    "mold list comprehension": Function(invoke_neosnippets, template_name="qlistcomp"),
}

extras = []
context = AppContext(title=".py") | CommandContext("python")
intellij_context = AppContext(executable="idea")
vscode_context = AppContext(executable="electron")
# TODO - Figure out how to scope this to just code
vim_context = AppContext(executable="iTerm2")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)

# # IntelliJ-specific mappings
Breathe.add_commands(
    context=context & intellij_context, mapping=intellij_mapping, extras=extras
)

# VSCode-specific mappings
Breathe.add_commands(
    context=context & vscode_context, mapping=vscode_mapping, extras=extras
)

# # Vim-specific mappings
# Breathe.add_commands(
#     context=context & vim_context, mapping=vim_mapping, extras=extras
# )
