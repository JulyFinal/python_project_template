from fastcore.script import call_parse, Param


@call_parse
def main(
    msg: Param("The message", str), upper: Param("Convert to uppercase?", bool) = False
):
    "Print `msg`, optionally converting to uppercase"
    print(msg.upper() if upper else msg)


# run examples/fastcore_cli.py --help
