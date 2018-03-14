# Rock your SublimeText with VIM keybindings and Sublimious!

[![Join the chat at https://gitter.im/dvcrn/sublimious](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dvcrn/sublimious?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

```
Sublimious is SublimeText 3 configuration system inspired by spacemacs and based around VIM.
```

__NOTE:__ Due to the SublimeText's uncertain future and slow development this project has been frozen and development shifted to atom with [proton](https://github.com/dvcrn/proton). If ST3's development picks up and long needed features are getting implemented, I will continue this project. Until then, PRs are welcome!

![Shortcuts](http://i.imgur.com/uvDjXNf.png)

### Install
Install `sublimious` through [package control](https://packagecontrol.io/packages/sublimious).

Currently sublimious is using the [Hack font face](https://github.com/chrissimpkins/Hack). If you don't have it installed, change `font_face` inside your `.sublimious` or download it here - https://github.com/chrissimpkins/Hack/releases. I can highly recommend you to install it though!

Alternatively, clone this repository into your `Packages/` directory if you prefer this method (good if you want to contribute :)!)

__Be warned__! Sublimious is a complete configuration system and will nuke your existing configuration. Make sure to backup your configs before trying sublimious!

### Features

Control everything with easy to remember shortcuts!

![showcase](http://i.imgur.com/MqsB6Pt.gif)

- __Preconfigured__: sublimious instantly makes sublime text better by shipping with a handful of hand-tested settings
- __VIM everywhere!__: All packages included with sublimious have been remapped to fit with vim keybindings
- __Easy to remember mnemonic__: Each command is mapped to a category / key combination that fits the action. `<spc> w v` for example splits the [__w__]indow [__v__]ertically.
- __Layer based configuration__: Check `layers/` for all configuration sets shipping with sublimious. Just add it to your `~/.sublimious` config and they will be included upon restart
- __Easy to use with dotfiles__: Just take your `~/.sublimious` config to your new pc and it will act exactly the same way as it did on your other pc
- __Central configuration__: Instead of maintaining 10 files, you only have 1 to put your settings in

### Keybindings

Sublimious comes with a keybinding helper to ease you in with everything. Just hit `space` and a popup will tell you what you can perform.

![keybindings](http://i.imgur.com/NBbFOCm.gif)

In general, sublimious follows the spacemacs mnemonic:
- `<spc> p` is for project commands
- `<spc> b` is for actions on the current buffer
- `<spc> g` is for git (needs git layer)
- `<spc> w` for window (splits and co)
- `<spc> s` for the current (visual) selection
- `<spc> e` for errors (linting)
- `<spc> t` is for toggles (sidebar, statusbar)
- `<spc> _` is for meta commands (sublimious reload)

Sublimious tries to add vim-like keybindings for every plugin possible. Sidebar navigation for example has been remapped to `j/k`.

### Tips and Tricks

- after changing your .sublimious file, hit `<spc> _ r` to re-feed your .sublimious config into sublimetext. All changes will be reloaded immediately. This includes packages, settings and layers.


### Contributing

There are a lot of things to do. Please check out the [issue tracker](https://github.com/dvcrn/sublimious/issues) and feel free to submit a pull request. 

For contributing guidelines, make sure you read the [CONTRIBUTING.md](https://github.com/dvcrn/sublimious/blob/master/.github/CONTRIBUTING.md) document.

### License

GPLv3
