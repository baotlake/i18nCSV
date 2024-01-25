<div align="center">
  <h1>i18nCSV</h1>
  <p>一个超级简单好用的跨平台 i18n 工具，在表格UI中轻松批量管理你的 i18n文件。提供i18n机器翻译、ChatGPT翻译、团队协作解决方案。</p>
  <p><a href="./README.md">English</a> | <a href="./README_ZH.md">中文</a></p>
</div>

## i18nCSV + CSV ：

-   表格 UI 界面
-   单一文本文件，支持 Git 版本管理

## i18nCSV + [Google Sheets](https://www.google.com/sheets/about/) :

-   支持 [Google Translate 翻译](https://support.google.com/docs/answer/3093331)
-   支持 ChatGPT GPT-3.5, GPT-4 翻译 (需要安装 [Google Workspace App](https://workspace.google.com/marketplace/search/gpt))
-   支持 人工翻译，团队协作翻译

## 为什么选择 i18nCSV

| 手动管理                                     | i18nCSV                                       |
| -------------------------------------------- | --------------------------------------------- |
| ❌ 编辑 JSON 代码，没有 UI                   | ✅ 支持表格 UI                                |
| ❌ 手动管理几十个语言的 JSON 文件            | ✅ 管理一份表格文档（CSV 或 Google Sheets）   |
| ❌ 新增/删除文案需要编辑每个语言的 JSON 文件 | ✅ 新增或者删除文案只需在表格中新增或删除一行 |
| ❌ 无法批量操作，无法自动翻译                | ✅ 支持选中几行或是几列，支持公式自动翻译     |
| ❌ 无法即时协作                              | ✅ 借助 Google Sheets，支持团队即时协作       |

## Usage

```txt
用法：i18ncsv.py [选项] I18N_DIR CSV_PATH

选项：
  -e, --extract          从i18n目录提取csv
  -n, --msg-name TEXT    i18n消息文件名
  -p, --prioritize TEXT  在CSV列的开头优先列出的语言，例如 'en,zh'。
  -o, --overwrite        覆盖现有的i18n消息，默认为False
  -w, --watch FLOAT      启用观察模式，当CSV文件更改时自动更新i18n
  --sheet-name TEXT      表的名称
  --range TEXT           任何有效的范围说明符，例如 A1:C99 或 B2:F
  --help                 显示此帮助消息并退出。
```

### 导出 CSV

由已有的 i18n Message 导出 CSV

```shell
python ./i18ncsv.py -e ./i18n i18n.csv
```

### 更新 i18n

```shell
# 从本地csv文件更新i18n
python ./i18ncsv.py ./i18n ./i18n.csv

# watch mode
python ./i18ncsv.py ./i18n ./i18n.csv -w

# 覆盖已有的i18n文件内容
python ./i18ncsv.py ./i18n ./i18n.csv -w -o

```

```shell
# 从Google Sheets文档更新i18n
# Google Sheets 应该设为知道链接的任何人都可以查看
python ./i18ncsv.py ./i18n https://docs.google.com/spreadsheets/d/xxxxxxxxxxx/ -w -o
```

更新 i18n 时也可以自动创建对应的文件，并通过`--msg-name`指定具体的目录结构，`<code>` 表示对应语言的 code。

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
