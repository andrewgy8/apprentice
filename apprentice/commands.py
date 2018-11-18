import click

MAIN_CONTENT = """from flask import Flask

from apprentice import format_response, generate_intent_response

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world(*args, **kwargs):
    phrase = "Hello there! I'm your Hello World Agent"
    formatted_data = generate_intent_response(phrase)
    return format_response(formatted_data)
"""

REQUIREMENTS_CONTENT = """apprentice
"""


@click.group()
def main():
    pass


@click.command(help='Show installed version')
def version():
    from .__version__ import __version__
    click.echo(f'Apprentice v{__version__}')


@click.command(help='Initialize a project')
def init():
    dir_name = 'hello_world_agent'
    import os
    if os.path.exists(dir_name):
        click.echo(f'{dir_name} already exists.')
        raise click.Abort()

    click.echo(f'Creating a project in {dir_name}')

    os.makedirs(dir_name)
    with open(f'{dir_name}/main.py', 'w') as file:
        file.write(MAIN_CONTENT)
        file.close()

    with open(f'{dir_name}/requirements.txt', 'w') as file:
        file.write(REQUIREMENTS_CONTENT)
        file.close()

    click.echo('Project created')


@click.command(help='Generate gcloud deploy command')
@click.option('--func', '-f', required=True, type=str,
              help='Name of Google Cloud Function')
@click.option('--source', '-s', required=True, type=click.Path(),
              help='Directory path to main.py')
@click.option('--entry_point', '-e', type=str, required=True,
              help='Function to be called in main.py')
@click.option('--region', '-r', type=str, default='us-central1',
              help='Google Cloud Compute Region')
def deploy(func, source, entry_point, region):
    base_command = 'gcloud functions deploy'

    deploy_command = f'{base_command} {func} --runtime python37 ' \
                     f'--trigger-http --source {source} ' \
                     f'--entry-point {entry_point} --region {region}'
    deploy_command = ' '.join(deploy_command.split())
    click.echo(f'Deploy with command: {deploy_command}')


main.add_command(version)
main.add_command(init)
main.add_command(deploy)
