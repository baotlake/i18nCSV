# Chrome Extension i18n Template

-   [locales.csv](./locales.csv)
-   [Google Sheets](https://docs.google.com/spreadsheets/d/1_nZ0P447OvpOiivrxmxSeHj3kUZtNzyUImXg5RB5v9U/)

## Generate `messages.json`

Use `locales.csv` to generate `messages.json` for each locale.

```bash
python i18ncsv.py ./_locales locales.csv --msg-name '<code>/messages.json'
```

Use Google Sheets to generate `messages.json` for each locale.

```bash
python i18ncsv.py ./_locales https://docs.google.com/spreadsheets/d/1_nZ0P447OvpOiivrxmxSeHj3kUZtNzyUImXg5RB5v9U/ --msg-name '<code>/messages.json'
```

## Export CSV from `messages.json`

```bash
python i18ncsv.py ./_locales ./locales.csv -e
```

## Locales

| Locale code | Language (region)                     |
| ----------- | ------------------------------------- |
| ar          | Arabic                                |
| am          | Amharic                               |
| bg          | Bulgarian                             |
| bn          | Bengali                               |
| ca          | Catalan                               |
| cs          | Czech                                 |
| da          | Danish                                |
| de          | German                                |
| el          | Greek                                 |
| en          | English                               |
| en_AU       | English (Australia)                   |
| en_GB       | English (Great Britain)               |
| en_US       | English (USA)                         |
| es          | Spanish                               |
| es_419      | Spanish (Latin America and Caribbean) |
| et          | Estonian                              |
| fa          | Persian                               |
| fi          | Finnish                               |
| fil         | Filipino                              |
| fr          | French                                |
| gu          | Gujarati                              |
| he          | Hebrew                                |
| hi          | Hindi                                 |
| hr          | Croatian                              |
| hu          | Hungarian                             |
| id          | Indonesian                            |
| it          | Italian                               |
| ja          | Japanese                              |
| kn          | Kannada                               |
| ko          | Korean                                |
| lt          | Lithuanian                            |
| lv          | Latvian                               |
| ml          | Malayalam                             |
| mr          | Marathi                               |
| ms          | Malay                                 |
| nl          | Dutch                                 |
| no          | Norwegian                             |
| pl          | Polish                                |
| pt_BR       | Portuguese (Brazil)                   |
| pt_PT       | Portuguese (Portugal)                 |
| ro          | Romanian                              |
| ru          | Russian                               |
| sk          | Slovak                                |
| sl          | Slovenian                             |
| sr          | Serbian                               |
| sv          | Swedish                               |
| sw          | Swahili                               |
| ta          | Tamil                                 |
| te          | Telugu                                |
| th          | Thai                                  |
| tr          | Turkish                               |
| uk          | Ukrainian                             |
| vi          | Vietnamese                            |
| zh_CN       | Chinese (China)                       |
| zh_TW       | Chinese (Taiwan)                      |

## Reference

-   [chrome.i18n](https://developer.chrome.com/docs/extensions/reference/api/i18n)
