class Layer():
    required_packages = [
        "GitGutter",
        "SublimeGit",
    ]

    keymap = [
        # ----- Git
        { "keys": [" ", "g", "s"], "command": "git_status", "args": {}, "context": [{"key": "setting.command_mode"}] },
        { "keys": [" ", "g", "p"], "command": "git_push", "args": {}, "context": [{"key": "setting.command_mode"}] },
        { "keys": ["j"], "command": "git_status_move", "args": {"goto": "item:next"}, "context": [{ "key": "selector", "operator": "equal", "operand": "text.git-status" }] },
        { "keys": ["k"], "command": "git_status_move", "args": {"goto": "item:prev"}, "context": [{ "key": "selector", "operator": "equal", "operand": "text.git-status" }] },
        { "keys": ["q"], "command": "close", "args": {}, "context": [{ "key": "selector", "operator": "equal", "operand": "text.git-status" }] },
    ]

    syntax_definitions = {}

    def init(self):
        pass
