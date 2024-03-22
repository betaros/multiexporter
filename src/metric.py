import reverse_geocode


def create_metric(data: dict, lat: float, lon: float):
    """
    Creates metrics

    :param data:
    :param lat:
    :param lon:
    :return:
    """

    values = []
    coordinates = ((lat, lon),)
    location = reverse_geocode.search(coordinates)[0]['city']

    for key, value in data.items():
        help_data = "# HELP " + key
        type_data = "# TYPE " + key
        message_data = 'openmeteo_' + key + '{location=\"' + location + '\"} ' + str(value)

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
