import requests
import datetime
import os
import logging

from PyFlightSearch.flight import Flight


QPX_API_KEY = os.environ.get('QPX_API_KEY')
QPX_HEADERS = {'Content-Type': 'application/json'}


def search(origin: str, destination: str, date: datetime.date, adults: int=1):
    url = ("https://www.googleapis.com/qpxExpress/v1/trips/search?key=" +
           QPX_API_KEY)
    data = {
        "request": {
            "passengers": {
                "kind": "qpxexpress#passengerCounts",
                "adultCount": adults,
            },
            "slice": [{
                "kind": "qpxexpress#sliceInput",
                "origin": origin,
                "destination": destination,
                "date": date.isoformat(),
            }],
            "refundable": "false",
            "solutions": 3
        }
    }

    response = requests.post(
        url.format(QPX_API_KEY), json=data, headers=QPX_HEADERS
    ).json()

    if 'trips' in response:
        return [
            Flight.from_qpx_json(flight_json) for flight_json in
            response['trips']['tripOption']
        ]

    # TODO: proper error handling
    logging.warning("Something went wrong with the response:")
    logging.warning(response)
