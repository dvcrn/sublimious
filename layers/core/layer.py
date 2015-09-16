from subprocess import call


class Layer():
    name = "Core"

    required_packages = [
        "Vintage-Origami",
        "Vintageous",
        "Origami",
        "Package Control",
        "SublimeLinter",
        "Surround",
        "Theme - Brogrammer",
        "Theme - Nil",
        "Theme - Soda",
        "Theme - Spacegray",
        "BracketHighlighter",
        "AdvancedNewFile",
    ]

    sublimious_keymap = [
        #----- Window commands
        # All these commands here will only work in command mode

        # Powered by Origami
        {"keys": ["w"], "category": "window"},
        {"keys": ["w", "v"], "command": "create_pane", "args": {"direction": "right"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "/"], "command": "create_pane", "args": {"direction": "right"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "s"], "command": "create_pane", "args": {"direction": "down"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "c"], "command": "destroy_pane", "args": {"direction": "self"}, "context": [{"key": "setting.command_mode"}]},

        # Panel navigation
        {"keys": ["w", "0"], "command": "focus_side_bar", "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "1"], "command": "focus_group", "args": {"group": 0}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "2"], "command": "focus_group", "args": {"group": 1}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "3"], "command": "focus_group", "args": {"group": 2}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "4"], "command": "focus_group", "args": {"group": 3}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "5"], "command": "focus_group", "args": {"group": 4}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "6"], "command": "focus_group", "args": {"group": 5}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "7"], "command": "focus_group", "args": {"group": 6}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "8"], "command": "focus_group", "args": {"group": 7}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["w", "9"], "command": "focus_group", "args": {"group": 8}, "context": [{"key": "setting.command_mode"}]},

        {"keys": ["0"], "command": "focus_side_bar", "context": [{"key": "setting.command_mode"}]},
        {"keys": ["1"], "command": "focus_group", "args": {"group": 0}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["2"], "command": "focus_group", "args": {"group": 1}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["3"], "command": "focus_group", "args": {"group": 2}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["4"], "command": "focus_group", "args": {"group": 3}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["5"], "command": "focus_group", "args": {"group": 4}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["6"], "command": "focus_group", "args": {"group": 5}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["7"], "command": "focus_group", "args": {"group": 6}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["8"], "command": "focus_group", "args": {"group": 7}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["9"], "command": "focus_group", "args": {"group": 8}, "context": [{"key": "setting.command_mode"}]},


        # ----- Project commands
        {"keys": ["p"], "category": "project"},
        {"keys": ["p", "t"], "command": "toggle_side_bar", "context": [{"key": "setting.command_mode"}]},
        {"keys": ["p", "f"], "command": "show_overlay", "args": {"overlay": "goto", "show_files": True}},
        {"keys": ["p", "c"], "command": "advanced_new_file_new", "context": [{"key": "setting.command_mode"}]},

        # ----- Buffers
        { "keys": ["tab"], "command": "prev_view_in_stack", "context": [{"key": "setting.command_mode"}]},

        # ----- Errors
        {"keys": ["e"], "category": "errors"},
        {"keys": ["e", "l"], "command": "sublimelinter_show_all_errors", "context": [{"key": "setting.command_mode"}]},
        {"keys": ["e", "n"], "command": "sublimelinter_goto_error", "args": {"direction": "next"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": ["e", "p"], "command": "sublimelinter_show_all_errors", "args": {"direction": "previous"}, "context": [{"key": "setting.command_mode"}]},

        # ----- Selection
        {"keys": ["s"], "category": "selection"},
        {"keys": ["s", "e"], "command": "find_all_under", "context": [{"key": "setting.command_mode"}]},

        # ----- Buffer
        {"keys": ["b"], "category": "buffer"},
        {"keys": ["b", "m"], "command": "advanced_new_file_move", "context": [{"key": "setting.command_mode"}]},
    ]

    sublime_keymap = [
        # Close everything with ESC
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_insert"}, "context": [{"key": "vi_insert_mode_aware"}]},
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_visual_line"}, "context": [{"key": "vi_mode_visual_line"}]},
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_visual"}, "context": [{"key": "vi_mode_visual"}]},

        {"keys": ["f", "d"], "command": "single_selection", "context": [{"key": "num_selections", "operator": "not_equal", "operand": 1}, {"key": "setting.command_mode"}]},
        {"keys": ["f", "d"], "command": "clear_fields", "context": [{"key": "has_next_field", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}]},
        {"keys": ["f", "d"], "command": "clear_fields", "context": [{"key": "has_prev_field", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}]},
        {"keys": ["f", "d"], "command": "hide_panel", "args": {"cancel": True}, "context": [{"key": "panel_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}]},
        {"keys": ["f", "d"], "command": "hide_overlay", "context": [{"key": "overlay_visible", "operator": "equal", "operand": True}]},
        {"keys": ["f", "d"], "command": "hide_popup", "context": [{"key": "popup_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}]},
        {"keys": ["f", "d"], "command": "hide_auto_complete", "context": [{"key": "auto_complete_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}]},

        # ----- Sidebar nav
        {"keys": ["h"], "command": "move", "args": {"by": "characters", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["l"], "command": "move", "args": {"by": "characters", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
    ]

    syntax_definitions = {
        "Python3": ['.sublimious']
   }

    def init(self, config):
        pass
