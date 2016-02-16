# Javascript Layer

Layer for adding javascript support and a bunch of linting.

## Requirements

- `tern`
- `flow`
- `jshint`
- `eslint`
- `jsbeautify`

## Configuration

The javascript layer comes with es6 and es5 mode. To use es6, set `use_es6` inside `.sublimious` to `True`.
If tern is not available global under `/usr/loca/bin/tern`, change the tern path by adding the following to your package_settings:

```
"Tern": {
    "tern_command": ["node", "/usr/local/bin/tern"],
}
```

## Usage

### General

`jshint`, `eslint` and friends will read your project specific `.eslintrc`, `jshintrc` and so on. If none is set, the normal default is being used.
