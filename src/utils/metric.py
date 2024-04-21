def create_metric(service: str, data: dict, parameter: str, parameter_value: str):
    """
    Creates metrics

    :param data:
    :param parameter:
    :param parameter_value:
    :return:
    """

    values = []

    for key, value in data.items():
        help_data = f"# HELP {service}_{key} The {' '.join(key.split('_'))}"
        type_data = f"# TYPE {service}_{key} gauge"
        message_data = f"{service}_{key}{{{parameter}={parameter_value}}} {str(value)}"

        values.append(help_data)
        values.append(type_data)
        values.append(message_data)

    return values
