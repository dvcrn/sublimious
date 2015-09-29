class Layer():
    name = "Git"

    required_packages = [
        "GitGutter",
        "GitSavvy",
    ]

    sublimious_keymap = [
        # ----- Git
        {"keys": ["g"], "category": "git"},
        {"keys": ["g", "s"], "command": "gs_show_status", "description": "status", "args": {}},
        {"keys": ["g", "P"], "command": "gs_push", "description": "push", "args": {}},
        {"keys": ["g", "p"], "command": "gs_pull", "description": "pull", "args": {}},
        {"keys": ["g", "n"], "command": "gs_checkout_new_branch", "description": "new branch", "args": {}},
        {"keys": ["g", "c"], "command": "gs_checkout_branch", "description": "checkout", "args": {}},
        {"keys": ["g", "l"], "command": "gs_log", "description": "log", "args": {}},
        {"keys": ["g", "f"], "command": "gs_fetch", "description": "fetch", "args": {}},
        {"keys": ["g", "a"], "command": "gs_commit", "description": "amend", "args": {"amend": True}},
        {"keys": ["g", "d"], "command": "gs_diff", "description": "diff", "args": {}},
    ]

    sublime_keymap = [
        {"keys": ["j"], "command": "gs_status_navigate_file", "args": {"forward": True}, "context": [{"key": "setting.git_savvy.status_view", "operator": "equal", "operand": True}]},
        {"keys": ["k"], "command": "gs_status_navigate_file", "args": {"forward": False}, "context": [{"key": "setting.git_savvy.status_view", "operator": "equal", "operand": True}]},
        {"keys": ["q"], "command": "close", "args": {}, "context": [{"key": "setting.git_savvy.status_view", "operator": "equal", "operand": True}]},
        {"keys": ["q"], "command": "close", "args": {}, "context": [{"key": "setting.git_savvy.diff_view", "operator": "equal", "operand": True}]},
        {"keys": ["q"], "command": "close", "args": {}, "context": [{"key": "setting.git_savvy.inline_diff_view", "operator": "equal", "operand": True}]},
    ]

    syntax_definitions = {}

    def init(self, config):
        pass
