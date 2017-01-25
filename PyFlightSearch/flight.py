import datetime
import attr


QPX_TIME_FORMAT = '%Y-%m-%dT%H%M%z'


def parse_qpx_time(time_str):
    # Format string can't deal with colons in the tz offset
    return datetime.datetime.strptime(time_str.replace(':', ''),
                                      QPX_TIME_FORMAT)


@attr.s
class Flight:
    origin = attr.ib(convert=str)
    dest = attr.ib(convert=str)
    currency = attr.ib(convert=str)
    price = attr.ib(convert=float)
    departure = attr.ib()
    arrival = attr.ib()

    @classmethod
    def from_qpx_json(cls, flight_json):
        origin_data = flight_json['slice'][0]['segment'][0]['leg'][0]
        dest_data = flight_json['slice'][-1]['segment'][-1]['leg'][-1]

        return cls(
            origin=origin_data['origin'],
            dest=dest_data['destination'],
            currency=flight_json['saleTotal'][:3],
            price=flight_json['saleTotal'][3:],
            departure=parse_qpx_time(origin_data['departureTime']),
            arrival=parse_qpx_time(dest_data['arrivalTime']),
        )
