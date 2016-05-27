# Rock your SublimeText with VIM keybindings and Sublimious!

[![Join the chat at https://gitter.im/dvcrn/sublimious](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dvcrn/sublimious?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

```
Sublimious is SublimeText 3 configuration system inspired by spacemacs and based around VIM.
```

__NOTE:__ Due to the SublimeTexts uncertain future and slow development this project has been frozen and development shifted to atom with [proton](https://github.com/dvcrn/proton). If ST3's development picks up and long needed features are getting implemented, I will continue this project. Until then, PRs are welcome!

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


### To-Dos:

- [x] get a basic version with space keybindings running
- [x] implement spacemacs-like shortcut helper
- [x] add README files for each layer
- [x] add a simple screenshot to README.md
- [x] add config for helper timeout to .sublimious
- [x] find a way to configure layers right out of .sublimious config
- [x] make `f <spc>` work
- [x] make `<spc> p f` work
- [x] add easier descriptions for commands
- [x] submit to package control
- [x] add install instructions to README
- [x] add a better default .sublimious
- [x] find a way to tell Package Control to reload (https://github.com/wbond/package_control/issues/997#issuecomment-141457037). This is needed to trigger pc after sublimious modified the pc settings file.
- [x] add option to reload .sublimious (trigger all layer collections, writings, and package control reload)
- [x] add option to define custom commands / functions inside layers
- [x] fix initial installation process (currently throwing a ton of errors)
- [ ] add option to add custom bindings to sublimious (e.g. user wants to bind action_123 to combination yyy). Should support both, sublimes system and sublimious system
- [ ] add option to pass parameters to a layer (eg `{layer: javascript, options: {foo:bar}}`)
- [ ] add option to execute / register functions from within .sublimious (e.g. user adds `def xxx` and wants to bind that function to combination yyy)
- [ ] allow multiple commands bound to the same key combination
- [ ] adjust the shortcut helper's width automagically
- [ ] ship Hack as default font and use it (possible?). If not, find a good preinstalled font and use that as default
- [ ] find a way to bind content specific actions to a keybinding. (e.g. `<space> m` will always list actions based on the current syntax. In javascript this could list `format javascript code` and in python `autoflake8`)


### License

GPLv3
