#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.

    To learn more about running Luigi, visit the Luigi project's
    `Read-The-Docs <http://luigi.readthedocs.io/en/stable/>`_ page.

.. currentmodule:: enip_scanner.cli
.. moduleauthor:: Jakub Kozerski <jakub.kozer@gmail.com>
"""
import logging
import click
from .__init__ import __version__

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


class Info(object):
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
#: pylint: disable=invalid-name
pass_info = click.make_pass_decorator(Info, ensure=True)


# Change the options to below to suit the actual options for your task (or
# tasks).
@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output.")
@pass_info
def cli(info: Info, verbose: int):
    """Run escanner."""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose


@cli.command()
@pass_info
def hello(_: Info):
    """Say 'hello' to the nice people."""
    click.echo("escanner says ''")


@cli.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))


@cli.command()
def art():
    ASCII_LOGO = """
   _____          __                                                            
  /  _  \ ______ |  | ______                                                     
 /  /_\  \\____ \|  |/ |__  \                                                    
/    |    \  |_> >    < / __ \_                                                  
\____|__  /   __/|__|_ (____  /                                                  
        \/|__|        \/    \/                                                   
            ________             __      ___.                                    
            \______ \   ____    |__| ____\_ |__ _____    ____ _____              
             |    |  \ /  _ \   |  |/ __ \| __ \\__  \  /    \\__  \             
             |    `   (  <_> )  |  \  ___/| \_\ \/ __ \|   |  \/ __ \_           
 ___________/_______  /\____/\__|  |\___  >___  (____  /___|  (____  /___________
/_____/_____/       \/      \______|    \/    \/     \/     \/     \/_____/_____/
"""

    click.echo(click.style(ASCII_LOGO, bold=True))