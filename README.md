<div align="center">
  <h1>i18nCSV</h1>
  <p>A super easy-to-use cross-platform i18n tool for efficiently managing your i18n files in a table UI. Provides i18n machine translation, ChatGPT translation, and team collaboration solutions.</p>
  <p><a href="./README.md">English</a> | <a href="./README_ZH.md">中文</a></p>
</div>

## i18nCSV + CSV:

-   Table UI interface
-   Single text file, supports Git version control

## i18nCSV + [Google Sheets](https://www.google.com/sheets/about/):

-   Supports [Google Translate translation](https://support.google.com/docs/answer/3093331)
-   Supports ChatGPT GPT-3.5, GPT-4 translation (requires installation of [Google Workspace App](https://workspace.google.com/marketplace/search/gpt))
-   Supports manual translation, team collaboration translation

## Why choose i18nCSV

| Manual Management                                                         | i18nCSV                                                                             |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| ❌ Edit JSON code without UI                                              | ✅ Supports table UI                                                                |
| ❌ Manually manage JSON files for dozens of languages                     | ✅ Manage a single table document (CSV or Google Sheets)                            |
| ❌ Adding/deleting messages requires editing JSON files for each language | ✅ Adding or deleting messages only requires adding or deleting a row in the table  |
| ❌ No batch operations, no automatic translation                          | ✅ Supports selecting rows or columns, supports automatic translation with formulas |
| ❌ No real-time collaboration                                             | ✅ With Google Sheets, supports real-time team collaboration                        |

## Usage

```txt
Usage: i18ncsv.py [OPTIONS] I18N_DIR CSV_PATH

Options:
  -e, --extract          extract csv from i18n directory
  -n, --msg-name TEXT    i18n message filename
  -p, --prioritize TEXT  Languages to prioritize at the beginning of CSV
                         columns, e.g., 'en,zh'.
  -o, --overwrite        overwrites existing i18n messages, default is False
  -w, --watch FLOAT      Enable watch mode to automatically update i18n when
                         the CSV file changes.
  --sheet-name TEXT      The name of the sheet
  --range TEXT           Any valid range specifier, e.g. A1:C99 or B2:F
  --help                 Show this message and exit.
```

### Export CSV

Export CSV from existing i18n messages.

```shell
python ./i18ncsv.py -e ./i18n i18n.csv
```

### Update i18n

```shell
# Update i18n from a local csv file
python ./i18ncsv.py ./i18n ./i18n.csv

# Watch mode
python ./i18ncsv.py ./i18n ./i18n.csv -w

# Overwrite existing i18n file content
python ./i18ncsv.py ./i18n ./i18n.csv -w -o

```

```shell
# Update i18n from a Google Sheets document
# Make sure to set Google Sheets to be viewable by anyone with the link
python ./i18ncsv.py ./i18n https://docs.google.com/spreadsheets/d/xxxxxxxxxxx/ -w -o
```

When updating i18n, you can automatically create corresponding files by specifying the directory structure through `--msg-name`, where `<code>` represents the code for the respective language.

```shell
python ./i18ncsv.py ./i18n ./i18n.csv --msg-name '<code>.json'

├── en.json
├── zh.json
├── ja.json
```

```shell
python ./i18ncsv.py ./i18n ./i18n.csv --msg-name '<code>/messages.json'

├── en
│   └── messages.json
├── zh
│   └── messages.json
├── ja
│   └── messages.json
```
