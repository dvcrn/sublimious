# Git Layer

![git](http://i.imgur.com/udkcPfB.gifv)

This layer adds basic git support and is powered by [GitSavvy](https://github.com/divmain/GitSavvy/).

## Requirements

- Git on your system

## Configuration

None yet. Check out [GitSavvy](https://github.com/divmain/GitSavvy/blob/master/GitSavvy.sublime-settings) for things you can change. 

To use github integration, add the following under your `package_settings` inside `.sublimious`:

```
"GitSavvy": {
    "api_tokens": {
        "github.com": "API TOKEN HERE"
    }
}
```

## Usage

### General

- `<spc> g s`: Git status
- `<spc> g p`: Git push
- `<spc> g c`: Git checkout
- `<spc> g n`: Git new branch
- `<spc> g f`: Git fetch
- `<spc> g l`: Git log
- `<spc> g a`: Git amend
- `<spc> g b`: Git blame

### Navigation

- `q` will close the `status` buffer
- navigation inside the `status` buffer is available with `j/k`
