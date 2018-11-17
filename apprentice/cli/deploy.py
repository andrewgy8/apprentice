import click


@click.command()
@click.option('--func', '-f', required=True, type=str)
@click.option('--source', '-s', type=str)
@click.option('--entry_point', '-e', type=str)
@click.option('--region', '-r', type=str, default='us-central1')
def deploy(func, source, entry_point, region):
    base_command = 'gcloud functions deploy'
    deploy_command = f'{base_command} {func} --runtime python37 ' \
                     f'--trigger-http --source {source} ' \
                     f'--entry-point {entry_point} --region {region}'

    click.echo(f'Deploy with command: {deploy_command}')
