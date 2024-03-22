def create_metric(data: dict, location: str):
    """
    Creates metrics

    :param data:
    :param location:
    :return:
    """

    values = []

    for key, value in data.items():
        help_data = "# HELP " + key
        type_data = "# TYPE " + key
        message_data = 'openmeteo_' + key + '{location=\"' + location + '\"} ' + str(value)

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
