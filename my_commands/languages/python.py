from my_commands.imports import *
from .intellij_support import invoke_live_template, run_action
from .vscode_support import invoke_snippet, run_vscode_action

mapping = {
    "pass": Text("pass"),
    "return": Text("return "),
    "break": Text("break"),
    "continue": Text("continue"),
    "self": Text("self"),
    "in it": Text("__init__"),
    "raise": Text("raise "),
    "none": Text("None"),
    "and": Text(" and "),
    "or": Text(" or "),
    "not": Text(" not "),
    "is not": Text(" is not "),
    "true": Text("True"),
    "false": Text("False"),
    "divide [by]": Text(" / "),
    "multiply [by]": Text(" * "),
    "exponent": Text(" ** "),
    "modulo": Text(" % "),
    "assign": Text(" = "),
    "is equal": Text(" == "),
    "is not equal": Text(" != "),
    "minus assign": Text(" -= "),
    "plus assign": Text(" += "),
    "greater equal": Text(" >= "),
    "lesser equal": Text(" <= "),
    "comment": Text("# "),
    "string": Text("str"),
    "integer": Text("int"),
    "boolean": Text("bool"),
    "float": Text("float"),
    "assert": Text("assert "),
    "dunder in it": Text("__init__"),
    # Requires my IntelliJ Live Templates
}

intellij_mapping = {
    "import": Function(invoke_live_template, template_name="qimport"),
    "import as": Function(invoke_live_template, template_name="qimportas"),
    "from import": Function(invoke_live_template, template_name="qfromimport"),
    "class": Function(invoke_live_template, template_name="qclass"),
    "method": Function(invoke_live_template, template_name="qmethod"),
    "private method": Function(invoke_live_template, template_name="qprivatemethod"),
    "dock string": Function(invoke_live_template, template_name="qdocstring"),
    "if": Function(invoke_live_template, template_name="qif"),
    "ell if": Function(invoke_live_template, template_name="qelif"),
    "else": Function(invoke_live_template, template_name="qelse"),
    "try": Function(invoke_live_template, template_name="qtry"),
    "(except | catch)": Function(invoke_live_template, template_name="qexcept"),
    "except as": Function(invoke_live_template, template_name="qexceptas"),
    "finally": Function(invoke_live_template, template_name="qfinally"),
    "for loop": Function(invoke_live_template, template_name="qfor"),
    "while": Function(invoke_live_template, template_name="qwhile"),
    "with": Function(invoke_live_template, template_name="qwith"),
    "with open": Function(invoke_live_template, template_name="qwithopen"),
    "format string": Function(invoke_live_template, template_name="qfstring"),
    "list comprehension": Function(invoke_live_template, template_name="qlistcomp"),
    # IntelliJ Actions
    "fix imports": Function(run_action, action_name="Optimize Imports"),
}

vscode_mapping = {
    "import": Function(invoke_snippet, template_name="qimportmod"),
    "import as": Function(invoke_live_template, template_name="qimportas"),
    "from import": Function(invoke_live_template, template_name="qfromimport"),
    "class": Function(invoke_live_template, template_name="qclass"),
    "method": Function(invoke_live_template, template_name="qmethod"),
    "private method": Function(invoke_live_template, template_name="qprivatemethod"),
    "dock string": Function(invoke_live_template, template_name="qdocstring"),
    "if": Function(invoke_live_template, template_name="qif"),
    "ell if": Function(invoke_live_template, template_name="qelif"),
    "else": Function(invoke_live_template, template_name="qelse"),
    "try": Function(invoke_live_template, template_name="qtry"),
    "(except | catch)": Function(invoke_live_template, template_name="qcatch"),
    "except as": Function(invoke_live_template, template_name="qexceptas"),
    "finally": Function(invoke_live_template, template_name="qfinally"),
    "for loop": Function(invoke_live_template, template_name="qfor"),
    "while": Function(invoke_live_template, template_name="qwhile"),
    "with": Function(invoke_live_template, template_name="qwith"),
    "with open": Function(invoke_live_template, template_name="qopenwith"),
    "format string": Function(invoke_live_template, template_name="qfstring"),
    "list comprehension": Function(invoke_live_template, template_name="qlistcomp"),
    # # IntelliJ Actions
    "fix imports": Function(run_action, action_name="Organize Imports"),
}

extras = []
context = AppContext(title=".py") | CommandContext("python")
intellij_context = AppContext(executable="idea")
vscode_context = AppContext(executable="electron")
# TODO - Figure out how to scope this to just code

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
