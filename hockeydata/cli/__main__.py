import click
from datetime import date

from hockeydata.cli.utils import check_date, check_season, OutputFormat
from hockeydata.api import get_game_shifts, get_season_play_by_play, get_play_by_plays, list_games, get_game_infos

@click.group()
def main():
    pass


@main.command(name="list-games", help="Gets game_ids for a date range")
@click.argument("start_date", default=str(date.today()), callback=check_date)
@click.argument("end_date", default=str(date.today()), callback=check_date)
@click.option(
    "-o",
    "--output-format",
    type=click.Choice(OutputFormat.options()),
    default="text",
    callback=OutputFormat.from_click_option,
)
def _list_games(start_date, end_date, output_format: OutputFormat):
    output_format.echo(list_games(start_date, end_date))

@main.command(name="shifts", help="Scrape a game for its shift data.")
@click.option(
    "-o", "--output-format",
    type=click.Choice(OutputFormat.options()),
    default="text",
    callback=OutputFormat.from_click_option,
)
@click.argument('game_ids', nargs=-1)
def _scrape_game(output_format: OutputFormat, game_ids):
    output_format.echo(get_game_shifts(*game_ids))

@main.command(name="game-info", help="Get high-level data about a game")
@click.option(
    "-o",
    "--output-format",
    type=click.Choice(OutputFormat.options()),
    default="text",
    callback=OutputFormat.from_click_option,
)
@click.argument('game_ids', nargs=-1)
def _game_info(output_format: OutputFormat, game_ids):
    output_format.echo(get_game_infos(*game_ids))

@main.command(name="shifts", help="Scrape a game for its shift data.")
@click.option(
    "-o", "--output-format",
    type=click.Choice(OutputFormat.options()),
    default="text",
    callback=OutputFormat.from_click_option,
)
@click.argument('game_ids', nargs=-1)
def _scrape_game(output_format: OutputFormat, game_ids):
    output_format.echo(get_game_shifts(*game_ids))


