# okcupid-search

Filters a list of profiles from OkCupid by some given parameters, so you don't have to spend a lifetime swiping.

### Features

* Filter by match percentage

That's all there is for now.

## Limitations

Note the effectiveness of this is limited by their app. I managed to find one of their endpoints that exposes enough profiles to filter through, but their algorithms are shit so almost all the results end up being poor matches anyway.

One potential workaround would be to run a headless Chrome (or other browser) instance, manually do the search, extract the relevant API response, then use this data to run the script. It could be run as a cron job and notify you when it finds any decent matches. You'd be able to leave it on autopilot with strong filters until it finds someone compatible. But I don't use OkCupid anymore so I'll leave this to someone if they want to make a PR.


## Installation

Install dependencies:

```sh
pipenv install --dev
```

Create an `.env` file for the settings:

```sh
cp .env.example .env
```

Then edit it with your preferred editor.

Open the pipenv shell:

```sh
pipenv shell
```

## How to use

### Getting data

First, you need to get a bunch of potential matches from OkCupid:

1. Open the [discovery page](https://www.okcupid.com/discovery) in your browser
2. Open the network inspector and filter by XHR requests
3. Search for a request where the `file` property is `section` is `high_percentage`
4. Edit and resend the request, and set the `limit` param to a huge number like `1000`
5. Copy and paste the results into a file named `data.json` in the project's directory

**Note:** the response results might be truncated if there's a huge amount of data. Therefore you may need to change a browser setting to stop data being redacted (instructions for this are out of the scope of this README).

### Using the script

Run the script:

```sh
python3 search.py
```

A list of IDs for each profile will be written into `matches.txt`.

Simply paste a given ID into the following link: `https://www.okcupid.com/profile/{id}`

### Options

Automatically open each match in your browser:

```sh
python3 search.py --open
```
