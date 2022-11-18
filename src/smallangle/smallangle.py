import click
import numpy as np
from numpy import pi
import pandas as pd







# def sin(number):
#     x = np.linspace(0, 2 * pi, number)
#     df = pd.DataFrame({"x": x, "{function} (x)": np.function(x)})
#     print(df)
#     return


# def tan(number):
#     x = np.linspace(0, 2 * pi, number)
#     df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
#     print(df)
#     return


@click.group()
def cmd_group():
    pass



@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)


def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

    return