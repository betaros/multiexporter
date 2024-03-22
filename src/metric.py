def create_metric(data: dict, location: str):
    """
    Creates metrics

    :param data:
    :param location:
    :return:
    """

    values = []

    for key, value in data.items():
        help_data = "# HELP openmeteo_" + key + " The " + " ".join(key.split('_'))
        type_data = "# TYPE openmeteo_" + key + " gauge"
        message_data = 'openmeteo_' + key + '{location=\"' + location + '\"} ' + str(value)

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
