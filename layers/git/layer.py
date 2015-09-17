class Layer():
    name = "Git"

    required_packages = [
        "GitGutter",
        "SublimeGit",
    ]

    sublimious_keymap = [
         #----- Git
        {"keys": ["g"], "category": "git"},
        {"keys": ["g", "s"], "command": "git_status", "args": {}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["g", "p"], "command": "git_push", "args": {}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["g", "n"], "command": "git_checkout_new_branch", "args": {}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["g", "c"], "command": "git_checkout_branch", "args": {}, "context": [{"key": "setting.command_mode"}]},
    ]

    sublime_keymap = [
        {"keys": ["j"], "command": "git_status_move", "args": {"goto": "item:next"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["k"], "command": "git_status_move", "args": {"goto": "item:prev"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["q"], "command": "close", "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["q"], "command": "close", "context": [{"key": "selector", "operator": "equal", "operand": "source.git-diff"}]},
    ]

    syntax_definitions = {}

    def init(self, config):
        pass
