import click
import numpy as np
from numpy import pi
import pandas as pd


#create the group for subcommando's
@click.group()
def cmd_group():
    pass


#first subcomando: sin function
#will run the function: sin(number) on command run_smallangle sin -n <number>
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)

#function sin(number) used in the first subcommand
def sin(number):
    """run through the sin of 0,2pi with number amount of steps
    Makes data frame out of the x and sin(x) values
    Prints dataframe

    Args:
        number (INTEGER): determines the amount of steps taken
    """   
  
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

#second subcommando: tan function
#will run the function: tan(number) on command run_smallangle tan -n <number>
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 1,
)

#function tan(number) used in the second subcommand
def tan(number):
    """run through the tan of 0,pi with number amount of steps
    Makes data frame out of the x and sin(x) values
    Prints dataframe

    Args:
        number (INTEGER): determines the amount of steps taken in the loop
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

    return