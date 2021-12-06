from my_commands.imports import *
from .intellij_support import invoke_live_template, run_action

mapping = {
    "mold local": Text("local."),
    "mold var": Text("var."),
    "mold module": Text("module."),
    "mold data": Text("data."),
    "mold comment": Text("# "),
    "mold and": Text(" && "),
    "mold or": Text(" || "),
    "mold true": Text("true"),
    "mold false": Text("false"),
    "mold divide [by]": Text(" / "),
    "mold multiply [by]": Text(" * "),
    "mold assign": Text(" = "),
    "mold is equal": Text(" == "),
    "mold is not equal": Text(" != "),
    "mold greater equal": Text(" >= "),
    "mold lesser equal": Text(" <= "),
    "mold string": Text("string"),
    "mold number": Text("number"),
    "mold boolean": Text("bool"),
    # Requires my IntelliJ Live Templates
    "mold create resource": Function(invoke_live_template, template_name="qresource"),
    "mold create module": Function(invoke_live_template, template_name="qmodule"),
    "mold create data": Function(invoke_live_template, template_name="qdata"),
    "mold create variable": Function(invoke_live_template, template_name="qvariable"),
    "mold create output": Function(invoke_live_template, template_name="qoutput"),
    "mold create locals": Function(invoke_live_template, template_name="qlocals"),
    "mold field": Function(invoke_live_template, template_name="qfield"),
    "mold block": Function(invoke_live_template, template_name="qblock"),
}
extras = []
context = AppContext(title=".tf") | CommandContext("terraform")

Breathe.add_commands(
    context=context,
    mapping=mapping,
    extras=extras,
)
