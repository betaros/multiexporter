def create_metric(service: str, data: dict, location: str):
    """
    Creates metrics

    :param data:
    :param location:
    :return:
    """

    values = []

    for key, value in data.items():
        help_data = "# HELP " + service + "_" + key + " The " + " ".join(key.split('_'))
        type_data = "# TYPE " + service + "_" + key + " gauge"
        message_data = service + "_" + key + '{location=\"' + location + '\"} ' + str(value)

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
