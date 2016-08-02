# Contribution guidelines

Thank you for your interest in contributing to this project! You rock!

Here are some smaller things to look out for when adding code to this repository

## Style guide

While not 100% there yet, make sure your code is pep8 / flake8 compliant. If you use sublimious to develop sublimious, you should automatically have the linters set up correctly to warn you about this.

## Commit format

Please use the following format to submit commits 
```
feat(ngInclude): add template url parameter to events

The `src` (i.e. the url of the template to load) is now provided to the
`$includeContentRequested`, `$includeContentLoaded` and `$includeContentError`
events.

Closes #8453
Closes #8454
```

```
                      component        commit title
        commit type       /                /      
                \        |                |
                 feat(ngInclude): add template url parameter to events

        body ->  The 'src` (i.e. the url of the template to load) is now provided to the
                 `$includeContentRequested`, `$includeContentLoaded` and `$includeContentError`
                 events.

 referenced  ->  Closes #8453
 issues          Closes #8454
```

For the commit type, use the matching type from this list:
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation

### Summary

Please use __present tense__ inside your commit message at all time. Keywords like `add` `fix` and friends should be in __lower case__ to keep things consistent.

### Linking to github

Here as well, please make sure that you use the __present tense__ for `Closes` and `Fixes` and add `References #XX` before referencing a github issue if you are not closing it. Please write these keywords in __uppercase__.

## Pull requests
Pull requests are currently submitted to `master`. This might change in the future so please keep an eye on this.
