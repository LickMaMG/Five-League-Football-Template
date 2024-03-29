import sys; sys.path.append("./")

from argparse import ArgumentParser
from src.calendars.laliga import LaLigaCalendar
from src.calendars.bundesliga import BundesligaCalendar
from src.calendars.ligue1 import Ligue1Calendar
from src.calendars.premierleague import PremierLeagueCalendar

CALENDARS = {
    "laliga": LaLigaCalendar,
    "liga": LaLigaCalendar,
    "ligue1": Ligue1Calendar,
    "bundesliga": BundesligaCalendar,
    "premierleague": PremierLeagueCalendar,
    "pl": PremierLeagueCalendar,
    # "seriea": SerieACalendar
}



def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "-l", "--league",
        type=str, required=True,
        help="Name of the league without space."
    )

    args = parser.parse_args()
    name = args.league.lower()
    CALENDARS.get(name)()


if __name__ == "__main__":
    main()