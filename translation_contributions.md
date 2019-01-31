# Contributing translations to Qiskit Terra and Qiskit Aqua

First, thank you! Translating these materials can help you learn the concepts at a new level while also making the project more accessible and available to everyone.

## Current translation efforts

As of February 2019, the we are working on updating the translated content for German, Japanese, Korean, and Chinese while also establishing a process for contributing future content that can grow with Qiskit, taking advantage of translation tools.

### Movement from `.rst` to using `gettext`

Previously, we were using .rst files that had translated versions of the existing text. This method works, but is not in a form where we can take advantage of translation tools, POEditors, which make coordinating large translation projects easier for both the doc publishers and translators. We're moving to using `gettext` as a different option. You can learn more about globalization and Sphinx by reading the [Internationalization docs](http://www.sphinx-doc.org/en/master/usage/advanced/intl.html).

## How do I help?

We now use the `sphinx-intl` package to pull the translatable text from our documentation and make it available in `.po` files. These files can be used in POEditor software, or you can simply translate in a text editor.

### Before you begin

You need a few tools before you can get started. Make sure that you have:

* [Python v3+](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)
* [Sphinx](https://pypi.org/project/Sphinx/)
* [sphinx-intl](https://pypi.org/project/sphinx-intl/)
* [git](https://git-scm.com/)
* [Sphinx Material Design theme](https://github.com/myyasuda/sphinx_materialdesign_theme)

Fork the [Qiskit docs repo](https://github.com/Qiskit/qiskit) and make a local clone. Change to your Qiskit repo `docs` directory.

## Contribute to translation

1. Extract translatable content into `.pot` files in the `gettext` directory.

  `make gettext`

1. Generate the `.po` source files in the `/locale` directory. These are the files you are going to translate. The following example creates .po source files for Japanese. You can add other languages by appending `-l LA` to the command.

  `sphinx-intl update -p _build/gettext -l ja`

1. Open the .po files you want to translate.

1. Add translated content into the `msgstr` strings.

  The `.po` files contain elements like `msgid` and `msgstr`. The English source is in `msgid`, and you can add your translations into `msgstr`. If no translation is needed, you can leave the `msgstr` blank. The following example shows a French translation.

  ```
  #: ../../theme/_templates/globaltoc.html:3
  msgid "Table Of Contents"
  msgstr "Table des Matiéres"
  ```

1. Add your changes to the `.pot` files.

  ```
  sphinx-intl update -p _build/locale
  ```

1. Commit your changes and make a PR.

## Building translations locally

You can build your translations locally by using a modified build command that specifies the `language` of the docs to be built.

  ```
  make -e SPHINXOPTS="-D language='ja'" html
  ```
