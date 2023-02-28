import pandas as pd


def lang(key: str) -> str:
    """Reads the file from assets/lang.json.

    Args:
        key (str): A key existing in lang.json.

    Returns:
        str: An application text.
    """
    return pd.read_json(path_or_buf='assets/lang.json', orient='index').to_dict()[0][key]
