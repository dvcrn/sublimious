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
        "Theme - Soda SolarizedDark",
        "InactivePanes"
    ]

    sublimious_keymap = [
        # ----- Window commands
        # All these commands here will only work in command mode

        # Powered by Origami
        {"keys": ["w"], "category": "window"},
        {"keys": ["w", "v"], "command": "create_pane", "args": {"direction": "right", "give_focus": True}},
        {"keys": ["w", "/"], "command": "create_pane", "args": {"direction": "right", "give_focus": True}},
        {"keys": ["w", "s"], "command": "create_pane", "args": {"direction": "down", "give_focus": True}},
        {"keys": ["w", "c"], "command": "destroy_pane", "args": {"direction": "self", "give_focus": True}},
        {"keys": ["w", "m"], "command": "set_layout", "args": {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]}},

        # Panel navigation
        {"keys": ["w", "0"], "command": "focus_side_bar"},
        {"keys": ["w", "1"], "command": "focus_group", "args": {"group": 0}},
        {"keys": ["w", "2"], "command": "focus_group", "args": {"group": 1}},
        {"keys": ["w", "3"], "command": "focus_group", "args": {"group": 2}},
        {"keys": ["w", "4"], "command": "focus_group", "args": {"group": 3}},
        {"keys": ["w", "5"], "command": "focus_group", "args": {"group": 4}},
        {"keys": ["w", "6"], "command": "focus_group", "args": {"group": 5}},
        {"keys": ["w", "7"], "command": "focus_group", "args": {"group": 6}},
        {"keys": ["w", "8"], "command": "focus_group", "args": {"group": 7}},
        {"keys": ["w", "9"], "command": "focus_group", "args": {"group": 8}},

        {"keys": ["l"], "command": "travel_to_pane", "args": {"direction": "right"}},
        {"keys": ["h"], "command": "travel_to_pane", "args": {"direction": "left"}},
        {"keys": ["j"], "command": "travel_to_pane", "args": {"direction": "down"}},
        {"keys": ["k"], "command": "travel_to_pane", "args": {"direction": "up"}},

        {"keys": ["0"], "command": "focus_side_bar"},
        {"keys": ["1"], "command": "focus_group", "args": {"group": 0}},
        {"keys": ["2"], "command": "focus_group", "args": {"group": 1}},
        {"keys": ["3"], "command": "focus_group", "args": {"group": 2}},
        {"keys": ["4"], "command": "focus_group", "args": {"group": 3}},
        {"keys": ["5"], "command": "focus_group", "args": {"group": 4}},
        {"keys": ["6"], "command": "focus_group", "args": {"group": 5}},
        {"keys": ["7"], "command": "focus_group", "args": {"group": 6}},
        {"keys": ["8"], "command": "focus_group", "args": {"group": 7}},
        {"keys": ["9"], "command": "focus_group", "args": {"group": 8}},


        # ----- Project commands
        {"keys": ["p"], "category": "project"},
        {"keys": ["p", "t"], "command": "toggle_side_bar"},
        {"keys": ["p", "f"], "command": "show_overlay", "args": {"overlay": "goto", "show_files": True}},
        {"keys": ["p", "c"], "command": "advanced_new_file_new"},

        # ----- Buffers
        {"keys": ["tab"], "command": "prev_view_in_stack"},

        # ----- Errors
        {"keys": ["e"], "category": "errors"},
        {"keys": ["e", "l"], "command": "sublimelinter_show_all_errors"},
        {"keys": ["e", "n"], "command": "sublimelinter_goto_error", "args": {"direction": "next"}},
        {"keys": ["e", "p"], "command": "sublimelinter_show_all_errors", "args": {"direction": "previous"}},

        # ----- Selection
        {"keys": ["s"], "category": "selection"},
        {"keys": ["s", "e"], "command": "find_all_under"},

        # ----- Buffer
        {"keys": ["b"], "category": "buffer"},
        {"keys": ["b", "m"], "command": "advanced_new_file_move"},

        # ----- Toggles
        {"keys": ["t"], "category": "toggles"},
        {"keys": ["t", "s"], "command": "toggle_status_bar"},
        {"keys": ["t", "t"], "command": "toggle_side_bar"},
    ]

    sublime_keymap = [
        # Close everything with ESC
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_insert"}, "context": [{"key": "vi_insert_mode_aware"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_visual_line"}, "context": [{"key": "vi_mode_visual_line"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "_enter_normal_mode", "args": {"mode": "mode_visual"}, "context": [{"key": "vi_mode_visual"}, {"key": "sublimious_chain"}]},

        {"keys": ["f", "d"], "command": "single_selection", "context": [{"key": "num_selections", "operator": "not_equal", "operand": 1}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "clear_fields", "context": [{"key": "has_next_field", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "clear_fields", "context": [{"key": "has_prev_field", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "hide_panel", "args": {"cancel": True}, "context": [{"key": "panel_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "hide_overlay", "context": [{"key": "overlay_visible", "operator": "equal", "operand": True}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "hide_popup", "context": [{"key": "popup_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},
        {"keys": ["f", "d"], "command": "hide_auto_complete", "context": [{"key": "auto_complete_visible", "operator": "equal", "operand": True}, {"key": "setting.command_mode"}, {"key": "sublimious_chain"}]},

        # ----- Sidebar nav
        {"keys": ["h"], "command": "move", "args": {"by": "characters", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["l"], "command": "move", "args": {"by": "characters", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
    ]

    syntax_definitions = {
        "Python": ['.sublimious']
    }

    def init(self, config):
        pass
