#! /usr/bin/env python

import click
import os
import json
import pandas as pd


@click.command()
@click.argument(
    "i18n_dir",
    envvar="I18N_DIR",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
)
@click.argument("csv_path", type=click.Path())
@click.option(
    "--extract", default=False, is_flag=True, help="extract csv from i18n directory"
)
@click.option("--msg-name", default="", help="i18n message filename")
@click.option(
    "--preference", default=["en"], multiple=True, help="preference languages"
)
@click.option("--overwrite", default=False, is_flag=True, help="")
def cli(
    i18n_dir: str,
    csv_path: str,
    extract=False,
    msg_name="",
    preference="",
    overwrite=False,
):
    locales_data = parse_locales(i18n_dir, msg_name)

    if extract:
        return extract_csv(
            locales_data["locales"],
            csv_path,
            preference,
        )

    data = {}
    translated = csv_path
    if translated.endswith(".csv"):
        df = pd.read_csv(translated, index_col=0).fillna("")
        data = denormalize(df.to_dict(orient="dict"))
    elif translated.endswith(".json"):
        with open(translated, "r", encoding="utf8") as f:
            data = json.load(f)
    elif translated.endswith(".jl"):
        with open(translated, "r", encoding="utf8") as f:
            for line in f:
                data = {**data, **json.load(line)}

    for code in data:
        filename = locales_data["msg_name"].replace("<code>", code)
        msg_path = os.path.join(i18n_dir, filename)
        update_msg(msg_path, data[code], overwrite=overwrite)


def parse_locales(i18n_dir: str, msg_name: str):
    dir_items = os.listdir(i18n_dir)
    codes = [os.path.splitext(i)[0] for i in dir_items]

    if len(dir_items) > 1 and not msg_name:
        if os.path.isfile(os.path.join(i18n_dir, dir_items[0])):
            msg_name = "<code>" + os.path.splitext(dir_items[0])[1]

        code_dir = os.path.join(i18n_dir, codes[0])
        if (not msg_name) and os.path.isdir(code_dir):
            items = os.listdir(code_dir)
            if len(items) == 1 and not os.path.isdir(items[0]):
                msg_name = f"<code>/{items[0]}"

    if not msg_name:
        msg_name = "<code>.json"

    locales = {c: os.path.join(i18n_dir, msg_name.replace("<code>", c)) for c in codes}

    return {
        "locales": locales,
        "msg_name": msg_name,
    }


def get_path(i18n_dir: str, item: str, filename: str):
    """parse path from listdir() or code and filename"""
    msg_path = os.path.join(i18n_dir, item)
    return os.path.join(msg_path, filename) if os.path.isdir(msg_path) else msg_path


def extract_csv(locales: dict, output: str, preference: list[str]):
    data = {}
    for code in list(dict.fromkeys([*preference, *locales.keys()])):
        with open(locales[code], "r", encoding="utf8") as f:
            data[code] = pd.json_normalize(json.load(f)).transpose()[0]
    df = pd.DataFrame(data)

    if output == "-":
        print(df.to_csv())
    else:
        df.to_csv(output)


def merge(base: dict, additional: dict):
    new = {**base, **additional}
    for k, v in additional.items():
        if isinstance(v, dict) and isinstance(new[k], dict):
            new[k] = merge(new[k], v)
    return new


def update_msg(msg_path: str, content: dict, overwrite=False):
    try:
        dir_path = os.path.dirname(msg_path)
        os.makedirs(dir_path, exist_ok=True)
        open_mode = "r+" if os.path.exists(msg_path) else "w+"
        with open(msg_path, open_mode, encoding="utf8") as f:
            msg = json.loads(f.read() or "{}")
            data = merge(msg, content) if not overwrite else content
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.truncate()
    except Exception as e:
        print("Error: ", msg_path)
        raise e


def denormalize(value: dict):
    data = {}
    for code, d in value.items():
        data[code] = {}
        for k, v in d.items():
            keys = k.split(".")
            current = data[code]
            for i, key in enumerate(keys):
                if i == len(keys) - 1:
                    current[key] = v
                    pass
                else:
                    current[key] = current[key] if key in current else {}
                    current = current[key]
    return data


if __name__ == "__main__":
    cli()
