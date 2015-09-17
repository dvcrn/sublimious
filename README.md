# Rock your SublimeText with VIM keybindings and Sublimious!

```
Sublimious is SublimeText 3 configuration system inspired by spacemacs and based around VIM.
```

![Shortcuts](http://i.imgur.com/2Yr2YeZ.gif)

### Install
for the moment, sublimious is not hosted on package control yet. To install, clone this repository into your `Packages` directory.

__Be warned__! Sublimious is a complete configuration system and will nuke your existing configuration. Make sure to backup your configs before trying sublimious!

### Configuration
By default, sublimious will read your `~/.sublimious` configuration file. If you don't have one yet, just copy the the `.sublimious` file out of this repository (under `template/`) and put it in your home directory. From now on, all you have to maintain is your sublimous config which will then take care of your sublime config.

### Keybindings

Sublimious comes with a keybinding helper to ease you in with everything. Just hit `space` and a popup will tell you what you can perform.

In general, sublimious follows the spacemacs mnemonic:
- `<spc> p` is for project commands
- `<spc> b` is for actions on the current buffer
- `<spc> g` is for git (needs git layer)
- `<spc> w` for window (splits and co)
- `<spc> s` for the current (visual) selection
- `<spc> e` for errors (linting)

Sublimious tries to add vim-like keybindings for every plugin possible. Sidebar navigation for example has been remapped to `j/k`.


### To-Dos:

- [x] get a basic version with space keybindings running
- [x] implement spacemacs-like shortcut helper
- [x] add README files for each layer
- [x] add a simple screenshot to README.md
- [ ] fix initial installation process (currently throwing a ton of errors)
- [ ] add config for helper timeout to .sublimious
- [ ] add a better default .sublimious
- [ ] adjust the shortcut helper's width automagically
- [ ] add better README files for each layer
- [ ] watch .sublimious file for changes and reload plugin
- [ ] find a way to tell Package Control to reload (necessary?)
- [ ] add a better default color scheme
- [ ] find a way to configure layers right out of .sublimious config
- [ ] add install instructions to README
- [ ] submit to package control
- [ ] add more layers
- [ ] add more shortcuts
