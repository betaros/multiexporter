def create_metric(service: str, data: dict, selector_name: str, selector_value: str):
    """
    Creates metrics

    :param service:
    :param data:
    :param selector_name:
    :param selector_value:
    :return:
    """

    values = []

    for key, value in data.items():
        help_data = "# HELP " + service + "_" + key + " The " + " ".join(key.split('_'))
        type_data = "# TYPE " + service + "_" + key + " gauge"
        message_data = service + "_" + key + '{' + selector_name + '=\"' + selector_value + '\"} ' + str(value)

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
