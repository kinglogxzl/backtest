@cli.command()
@click.option('-f', '--strategy-file', type=click.Path(exists=True), required=True)
@click.option('-s', '--start-date', type=Date(), required=True)
@click.option('-e', '--end-date', type=Date(), required=True)
def run(strategy_file, start_date, end_date):
    print strategy_file
    print start_date
    print end_date
