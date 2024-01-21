# i18nCSV

```txt
Usage: i18ncsv.py [OPTIONS] I18N_DIR CSV_PATH

Options:
  --extract            extract csv from i18n directory
  --msg-name TEXT      i18n message filename
  --preference TEXT    preference languages
  --overwrite BOOLEAN
  --help               Show this message and exit.
```

## Examples

### Extract CSV from i18n directory

```shell
python ./i18ncsv.py --extract examples i18n.csv
```

### Update i18n message

```shell
python ./i18ncsv.py examples i18n.csv
```
