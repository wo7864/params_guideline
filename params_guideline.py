import argparse

import json
import yaml

SUPPRESS = '==SUPPRESS=='


class _jsonParserAction(argparse.Action,argparse._ActionsContainer):

    def __init__(self,
                 option_strings,
                 dest,
                 prog=None,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None,
                 prefix_chars='-',
                 description=None,
                 argument_default=None,
                 conflict_handler='error',
                 ):
        argparse.Action.__init__(
            self,
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            const=const,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar)

        argparse._ActionsContainer.__init__(self,
                 description,
                 prefix_chars,
                 argument_default,
                 conflict_handler)
        self._prog_prefix = prog
        self.prefix_chars = prefix_chars
        self.file_path = None
        def identity(string):
            return string
        self.register('type', None, identity)
        
    def __call__(self, parser, namespace, values, option_string=None):
        self.file_path = values
        sub_namespace = argparse.Namespace()
        with open(self.file_path, 'r') as f:
            parse_json = json.load(f)

        for sub_action in self._actions:
            try:
                sub_action_value = parse_json[sub_action.dest]
            except:
                if not sub_action.option_strings: 
                    raise KeyError(f"{sub_action.dest} is not included in {self.file_path} JSON File.")
            else:
                sub_action(self, sub_namespace, sub_action_value)

        setattr(namespace, self.dest, sub_namespace)


class _yamlParserAction(argparse.Action,argparse._ActionsContainer):

    def __init__(self,
                 option_strings,
                 dest,
                 prog=None,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None,
                 prefix_chars='-',
                 description=None,
                 argument_default=None,
                 conflict_handler='error',
                 ):
        argparse.Action.__init__(
            self,
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            const=const,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar)

        argparse._ActionsContainer.__init__(self,
                 description,
                 prefix_chars,
                 argument_default,
                 conflict_handler)
        self._prog_prefix = prog
        self.prefix_chars = prefix_chars
        self.file_path = None
        def identity(string):
            return string
        self.register('type', None, identity)
        
    def __call__(self, parser, namespace, values, option_string=None):
        self.file_path = values
        sub_namespace = argparse.Namespace()
        with open(self.file_path, 'r') as f:
            parse_json = yaml.load(f, Loader=yaml.FullLoader)

        for sub_action in self._actions:
            try:
                sub_action_value = parse_json[sub_action.dest]
            except:
                if not sub_action.option_strings: 
                    raise KeyError(f"{sub_action.dest} is not included in {self.file_path} YAML File.")
            else:
                sub_action(self, sub_namespace, sub_action_value)

        setattr(namespace, self.dest, sub_namespace)


class CustomHelpFormatter(argparse.HelpFormatter):
    
    def add_argument(self, action):
        super(CustomHelpFormatter, self).add_argument(action)

        if type(action) is _jsonParserAction:
            self.start_section(f'*{action.dest} detail')
            for sub_action in action._actions:
                self.add_argument(sub_action)
            self.end_section()
                

class Parser(argparse.ArgumentParser):

    def __init__(self, **kwargs):
        kwargs['formatter_class']=CustomHelpFormatter
        super(Parser, self).__init__(**kwargs)
        self.register('action', 'json_parser', _jsonParserAction)
        self.register('action', 'yaml_parser', _yamlParserAction)


    def add_json_parser(self, *args, **kwargs):
        kwargs['action'] = 'json_parser'
        action = super(Parser, self).add_argument(*args, **kwargs)
        return action

    def add_yaml_parser(self, *args, **kwargs):
        kwargs['action'] = 'yaml_parser'
        action = super(Parser, self).add_argument(*args, **kwargs)
        return action
