# Build an Interactive Dictionary (CLI)
## Task
Build a command line application which will use the `.json` dataset, found [here](https://github.com/matthewreagan/WebstersEnglishDictionary), to return the definition of an English word which the user inputs.

The `.json` file must me converted into a `dictionary` using the `json` library.

If the user inputs an invalid word, the program must suggest close valid matches to this input using the `get_close_matches` method from the `difflib` library.

Also, keep in mind the case sensitivity of the `json` dataset and how that might affect the program.

The command line aspect  will not do the program any mercy in terms of a good UI, but try your best to make the app as user intuitive as possible.

## Examples
`definitionOfWord(voltage) ➞ "Electric potential or potential difference, expressed in volts."`

`definitionOfWord(amperge) ➞ "Did you mean amperage instead?"`