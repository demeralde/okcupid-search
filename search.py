import argparse
import json
import os
import webbrowser

from dotenv import load_dotenv


# Init
load_dotenv()
parser = argparse.ArgumentParser("search")
parser.add_argument(
    "--open",
    default=False,
    help="Opens results in your default browser",
    action="store_true"
)
args = parser.parse_args()

# Constants
MATCH_PERCENTAGE = int(os.getenv("MATCH_PERCENTAGE"))
OKCUPID_PROFILE_ROUTE = "https://www.okcupid.com/profile/"
MATCHES_FILE = "matches.txt"


def main():
    data = open("data.json", "r")
    data_json = json.load(data)

    all_results = data_json["results"]["rows"][0]["data"]
    matches = list(
        filter(
            lambda result: result["percentages"]["match"] >= MATCH_PERCENTAGE, all_results
        )
    )
    match_ids = list(map(lambda match: match["userid"], matches))

    with open(MATCHES_FILE, "w+") as file:
        for match_id in match_ids:
            file.write(f'{match_id}\n')
            if args.open:
                webbrowser.open(f"{OKCUPID_PROFILE_ROUTE}{match_id}", new=2)

    print(f"{len(match_ids)} matches found and saved to {MATCHES_FILE}")
    if args.open:
        print("opened results in browser")


if __name__ == "__main__":
    main()
