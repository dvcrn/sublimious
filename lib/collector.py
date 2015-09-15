import itertools

def collect_syntax_specific_settings(layers):
    syntax_definitions = {}

    for layer in layers:
        if not hasattr(layer, "syntax_definitions"):
            continue

        for syntax, files in layer.syntax_definitions.items():
            if syntax not in syntax_definitions:
                syntax_definitions[syntax] = {"extensions": []}

            syntax_definitions[syntax]["extensions"] = syntax_definitions[syntax]["extensions"] + files



        if not hasattr(layer, "color_scheme_definitions"):
            continue

        for syntax, color_schemes in layer.color_scheme_definitions.items():
            if syntax not in syntax_definitions:
                syntax_definitions[syntax] = {"color_scheme": []}

            if "color_scheme" not in syntax_definitions[syntax]:
                syntax_definitions[syntax]["color_scheme"] = color_schemes

    return syntax_definitions

def collect_key(layers, key):
    collected_list = list(map(lambda i: getattr(i, key), layers))
    return list(itertools.chain(*collected_list))
