from subprocess import call

class Layer():
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

    keymap = [
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

        # ----- Window commands
        # Window management powered by Origami
        {"keys": [" ", "w", "v"], "command": "create_pane", "args": {"direction": "right"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": [" ", "w", "/"], "command": "create_pane", "args": {"direction": "right"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": [" ", "w", "s"], "command": "create_pane", "args": {"direction": "down"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": [" ", "w", "c"], "command": "destroy_pane", "args": {"direction": "self"}, "context": [{"key": "setting.command_mode"}]},

        # Panel navigation
        {"keys": [" ", "w", "0"], "command": "focus_side_bar"},
        {"keys": [" ", "w", "1"], "command": "focus_group", "args": {"group": 0}},
        {"keys": [" ", "w", "2"], "command": "focus_group", "args": {"group": 1}},
        {"keys": [" ", "w", "3"], "command": "focus_group", "args": {"group": 2}},
        {"keys": [" ", "w", "4"], "command": "focus_group", "args": {"group": 3}},
        {"keys": [" ", "w", "5"], "command": "focus_group", "args": {"group": 4}},
        {"keys": [" ", "w", "6"], "command": "focus_group", "args": {"group": 5}},
        {"keys": [" ", "w", "7"], "command": "focus_group", "args": {"group": 6}},
        {"keys": [" ", "w", "8"], "command": "focus_group", "args": {"group": 7}},
        {"keys": [" ", "w", "9"], "command": "focus_group", "args": {"group": 8}},


        # ----- Project commands
        {"keys": [" ", "p", "t"], "command": "toggle_side_bar"},
        {"keys": [" ", "p", "f"], "command": "show_overlay", "args": {"overlay": "goto", "show_files": True}},
        {"keys": [" ", "p", "c"], "command": "advanced_new_file_new"},

        # ----- Sidebar nav
        {"keys": ["h"], "command": "move", "args": {"by": "characters", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [{"key": "control", "operand": "sidebar_tree"}]},
        {"keys": ["l"], "command": "move", "args": {"by": "characters", "forward": True}, "context": [{"key": "control", "operand": "sidebar_tree"}]},

        # ----- Buffers
        { "keys": [" ", "tab"], "command": "prev_view_in_stack", "context": [{"key": "setting.command_mode"}]},

        # ----- Errors
        {"keys": [" ", "e", "l"], "command": "sublimelinter_show_all_errors", "context": [{"key": "setting.command_mode"}]},
        {"keys": [" ", "e", "n"], "command": "sublimelinter_goto_error", "args": {"direction": "next"}, "context": [{"key": "setting.command_mode"}]},
        {"keys": [" ", "e", "p"], "command": "sublimelinter_show_all_errors", "args": {"direction": "previous"}, "context": [{"key": "setting.command_mode"}]},
    ]

    syntax_definitions = {
        "Python3": ['.sublimious']
   }

    def init(self, config):
        pass
