import click

from .cli import deploy, initialize


@click.group()
def main():
    pass


@click.command()
def version():
    from .__version__ import __version__
    click.echo(f'Apprentice {__version__}')
    pass


main.add_command(version)
main.add_command(initialize.init)
main.add_command(deploy.deploy)
