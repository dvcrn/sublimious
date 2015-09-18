class Layer():
    name = "Git"

    required_packages = [
        "GitGutter",
        "SublimeGit",
    ]

    sublimious_keymap = [
        # ----- Git
        {"keys": ["g"], "category": "git"},
        {"keys": ["g", "s"], "command": "git_status", "description": "status", "args": {}},
        {"keys": ["g", "p"], "command": "git_push", "description": "push", "args": {}},
        {"keys": ["g", "n"], "command": "git_checkout_new_branch", "description": "new branch", "args": {}},
        {"keys": ["g", "c"], "command": "git_checkout_branch", "description": "checkout", "args": {}},
        {"keys": ["g", "l"], "command": "git_log", "description": "log", "args": {}},
        {"keys": ["g", "f"], "command": "git_fetch", "description": "fetch", "args": {}},
        {"keys": ["g", "a"], "command": "git_commit_amend", "description": "amend", "args": {}},
    ]

    sublime_keymap = [
        {"keys": ["j"], "command": "git_status_move", "args": {"goto": "item:next"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["k"], "command": "git_status_move", "args": {"goto": "item:prev"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["q"], "command": "close", "context": [{"key": "selector", "operator": "equal", "operand": "text.git-status"}]},
        {"keys": ["q"], "command": "close", "context": [{"key": "selector", "operator": "equal", "operand": "source.git-diff"}]},
        {"keys": ["q"], "command": "close", "context": [{"key": "selector", "operator": "equal", "operand": "source.git-status"}]},
    ]

    syntax_definitions = {}

    def init(self, config):
        pass
