class Layer():
    name = "Core"

    required_packages = [
        "sublimious",
        "Package Control",
        "Vintage-Origami",
        "Vintageous",
        "Vintageous​Plugin​Surround",
        "Origami",
        "SublimeLinter",
        "Surround",
        "BracketHighlighter",
        "AdvancedNewFile",
        "InactivePanes",
        "Theme - Soda SolarizedDark",
        "Tab Filter",
    ]

    sublimious_keymap = [
        # ----- Window commands
        # All these commands here will only work in command mode

        # Powered by Origami
        {"keys": ["w"], "category": "window"},
        {"keys": ["w", "v"], "command": "create_pane", "description": "split vertically", "args": {"direction": "right", "give_focus": True}},
        {"keys": ["w", "/"], "command": "create_pane", "description": "split vertically", "args": {"direction": "right", "give_focus": True}},
        {"keys": ["w", "s"], "command": "create_pane", "description": "split horizontally", "args": {"direction": "down", "give_focus": True}},
        {"keys": ["w", "c"], "command": "destroy_pane", "description": "close window", "args": {"direction": "self", "give_focus": True}},
        {"keys": ["w", "m"], "command": "set_layout", "description": "maximise window", "args": {"cells": [[0, 0, 1, 1]], "cols": [0.0, 1.0], "rows": [0.0, 1.0]}},

        # Panel navigation
        {"keys": ["w", "0"], "command": "focus_side_bar", "description": "focus side bar"},
        {"keys": ["w", "1"], "command": "focus_group", "description": "focus window 1", "args": {"group": 0}},
        {"keys": ["w", "2"], "command": "focus_group", "description": "focus window 2", "args": {"group": 1}},
        {"keys": ["w", "3"], "command": "focus_group", "description": "focus window 3", "args": {"group": 2}},
        {"keys": ["w", "4"], "command": "focus_group", "description": "focus window 4", "args": {"group": 3}},
        {"keys": ["w", "5"], "command": "focus_group", "description": "focus window 5", "args": {"group": 4}},
        {"keys": ["w", "6"], "command": "focus_group", "description": "focus window 6", "args": {"group": 5}},
        {"keys": ["w", "7"], "command": "focus_group", "description": "focus window 7", "args": {"group": 6}},
        {"keys": ["w", "8"], "command": "focus_group", "description": "focus window 8", "args": {"group": 7}},
        {"keys": ["w", "9"], "command": "focus_group", "description": "focus window 9", "args": {"group": 8}},

        {"keys": ["l"], "command": "travel_to_pane", "description": "focus right pane", "args": {"direction": "right"}},
        {"keys": ["h"], "command": "travel_to_pane", "description": "focus left pane", "args": {"direction": "left"}},
        {"keys": ["j"], "command": "travel_to_pane", "description": "focus down pane", "args": {"direction": "down"}},
        {"keys": ["k"], "command": "travel_to_pane", "description": "focus up pane", "args": {"direction": "up"}},

        {"keys": ["0"], "command": "focus_side_bar", "description": "focus side bar"},
        {"keys": ["1"], "command": "focus_group", "description": "focus window 1", "args": {"group": 0}},
        {"keys": ["2"], "command": "focus_group", "description": "focus window 2", "args": {"group": 1}},
        {"keys": ["3"], "command": "focus_group", "description": "focus window 3", "args": {"group": 2}},
        {"keys": ["4"], "command": "focus_group", "description": "focus window 4", "args": {"group": 3}},
        {"keys": ["5"], "command": "focus_group", "description": "focus window 5", "args": {"group": 4}},
        {"keys": ["6"], "command": "focus_group", "description": "focus window 6", "args": {"group": 5}},
        {"keys": ["7"], "command": "focus_group", "description": "focus window 7", "args": {"group": 6}},
        {"keys": ["8"], "command": "focus_group", "description": "focus window 8", "args": {"group": 7}},
        {"keys": ["9"], "command": "focus_group", "description": "focus window 9", "args": {"group": 8}},


        # ----- Project commands
        {"keys": ["p"], "category": "project"},
        {"keys": ["p", "t"], "command": "toggle_side_bar", "description": "toggle sidebar"},
        {"keys": ["p", "f"], "command": "show_overlay", "description": "find file", "args": {"overlay": "goto", "show_files": True}},
        {"keys": ["p", "c"], "command": "advanced_new_file_new", "description": "create file"},

        # ----- Buffers
        {"keys": ["tab"], "command": "next_view", "description": "previous buffer"},

        # ----- Errors
        {"keys": ["e"], "category": "errors"},
        {"keys": ["e", "l"], "command": "sublimelinter_show_all_errors", "description": "list lint errors"},
        {"keys": ["e", "n"], "command": "sublimelinter_goto_error", "description": "next lint error", "args": {"direction": "next"}},
        {"keys": ["e", "p"], "command": "sublimelinter_show_all_errors", "description": "prev lint error", "args": {"direction": "previous"}},

        # ----- Selection
        {"keys": ["s"], "category": "selection"},
        {"keys": ["s", "e"], "command": "find_all_under", "description": "expand selection"},

        # ----- Buffer
        {"keys": ["b"], "category": "buffer"},
        {"keys": ["b", "m"], "command": "advanced_new_file_move", "description": "move/rename file"},
        {"keys": ["b", "b"], "command": "tab_filter", "description": "navigate buffers"},

        # ----- Toggles
        {"keys": ["t"], "category": "toggles"},
        {"keys": ["t", "s"], "command": "toggle_status_bar", "description": "toggle statusbar"},
        {"keys": ["t", "t"], "command": "toggle_side_bar", "description": "toggle sidebar"},
        {"keys": ["t", "l"], "command": "toggle_setting", "args": {"setting": "line_numbers"}, "description": "toggle line numbers"},
        {"keys": ["t", "m"], "command": "toggle_minimap", "args": {}, "description": "toggle minimap"},
        {"keys": ["t", "t"], "command": "toggle_tabs", "args": {}, "description": "toggle tabs"},

        # ----- Meta
        {"keys": ["_"], "category": "meta"},
        {"keys": ["_", "r"], "command": "reload_sublimious", "description": "reload .sublimious"},
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
