def parse_args(raw_text: str):
    """

    :param raw_text: must be like "--key1 value1 --key2 value2"
    :return: {"key1": "value1", "key2": "value2"}
    """
    params = dict()
    args = list(filter(None, raw_text.replace(' —', '—').split('—')))
    for arg in args:
        key_values = arg.split(' ')
        assert len(key_values) == 2
        params[key_values[0]] = key_values[1]
    return params


def validate_data(data):
    chat_id = data.get('chat_id')
    text = data.get('text')
    return bool(chat_id and text)
