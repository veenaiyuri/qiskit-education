# Localization Strategy: Contributing translations to Qiskit

First, thank you! Translating these materials can help you learn the concepts at a new level while also making the project more accessible and available to everyone.

## 1. Current translation efforts

As of February 2019, we are working on updating the translated content for German, Japanese, Korean, and Chinese while also establishing a process for contributing future content that can grow with Qiskit, taking advantage of translation tools.

### 2. Movement from `.rst` to using `gettext`

Previously, we were using .rst files that had translated versions of the existing text. This method works, but is not in a form where we can take advantage of translation tools, POEditors, which make coordinating large translation projects easier for both the doc publishers and translators. We're moving to using `gettext` as a different option. You can learn more about globalization and Sphinx by reading the [Internationalization docs](http://www.sphinx-doc.org/en/master/usage/advanced/intl.html).

## 3. How do I help?

We now use the `sphinx-intl` package to pull the translatable text from our documentation and make it available in `.po` files. These files can be used in POEditor software, or you can simply translate in a text editor.

### 4. Before you begin

You need a few tools before you can get started. Make sure that you have:

* [Python v3+](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Sphinx](https://pypi.org/project/Sphinx/)
* [sphinx-intl](https://pypi.org/project/sphinx-intl/)
* [git](https://git-scm.com/)
* [Sphinx Material Design theme](https://github.com/myyasuda/sphinx_materialdesign_theme)

Fork the [Qiskit docs repo](https://github.com/Qiskit/qiskit) and make a local clone. Change to your Qiskit repo `docs` directory.

## 5. Contribute to translation

1. Open Terminal. Make sure you are in your `docs` directory under your local Qiskit repo and type `make gettext` at your terminal to extract translatable content into `.pot` files in the `_build/gettext` directory.

  `$ make gettext`

2. Generate the `.po` source files in the `/locales` directory. These are the files you are going to translate. The following example creates .po source files for Japanese. You can add other languages by appending `-l LA` to the command.

  `$ sphinx-intl update -p _build/gettext -l ja`

3. Under `locales/ja/LC_MESSAGES/` open the .po files you want to translate. Copy these to a source directory if necessary.

  For members who would like to use translation tools to contribute to this project, please refer to section 7 of this document page.

4. Add translated content into the `msgstr` strings.

  The `.po` files contain elements like `msgid` and `msgstr`. The English source is in `msgid`, and you can add your translations into `msgstr`. If no translation is needed, you can leave the `msgstr` blank. The following example shows a French translation.

  ```
  #: ../../theme/_templates/globaltoc.html:3
  msgid "Table Of Contents"
  msgstr "Table des Matiéres"
  ```

5. Add your changes to the `.pot` files.

  ```
  sphinx-intl update -p _build/locales
  ```

6. Commit your changes and make a PR.

## 6. Building translations locally

You can build your translations locally by using a modified build command that specifies the `language` of the docs to be built.

  ```
  make -e SPHINXOPTS="-D language='ja'" html
  ```
## 7. Using Translation Tools

You can use translation tools or so called localization management platforms such as [Crowdin](https://crowdin.com/) to crowd source translation efforts and take advantage of Machine Translation and Translation Memory (TM) to speed up the task.

Please contact [Yuri Kobayashi](mailto:yurik@jp.ibm.com)if you are interested in participating in using a translation tool to make contributions to Qiskit localization.
