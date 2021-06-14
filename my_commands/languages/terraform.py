from my_commands.imports import *
from .intellij_support import invoke_live_template, run_action

mapping = {
    "local": Text("local."),
    "var": Text("var."),
    "module": Text("module."),
    "data": Text("data."),
    "comment": Text("# "),
    "and": Text(" && "),
    "or": Text(" || "),
    "true": Text("true"),
    "false": Text("false"),
    "divide [by]": Text(" / "),
    "multiply [by]": Text(" * "),
    "assign": Text(" = "),
    "is equal": Text(" == "),
    "is not equal": Text(" != "),
    "greater equal": Text(" >= "),
    "lesser equal": Text(" <= "),
    "string": Text("string"),
    "number": Text("number"),
    "boolean": Text("bool"),
    # Requires my IntelliJ Live Templates
    "create resource": Function(invoke_live_template, template_name="qresource"),
    "create module": Function(invoke_live_template, template_name="qmodule"),
    "create data": Function(invoke_live_template, template_name="qdata"),
    "create variable": Function(invoke_live_template, template_name="qvariable"),
    "create output": Function(invoke_live_template, template_name="qoutput"),
    "create locals": Function(invoke_live_template, template_name="qlocals"),
    "field": Function(invoke_live_template, template_name="qfield"),
    "block": Function(invoke_live_template, template_name="qblock"),
}
extras = []
context = AppContext(title=".tf") | CommandContext("terraform")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)