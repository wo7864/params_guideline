from params_guideline import Parser

parser = Parser(description='Process some integers.', exit_on_error=False)
json_parser = parser.add_json_parser('--configs', required=True, help='config json file')
json_parser.add_argument('test', type=str, help="test")
json_parser.add_argument('--test2', type=str, help="test")

json_parser = parser.add_json_parser('--yaml_config', required=True, help='config yaml file')
json_parser.add_argument('isyaml', type=str, help="test")
json_parser.add_argument('--hello', type=str, help="test")

args = parser.parse_args()
print('fin:', args)
print('fin:', args.configs.test)
