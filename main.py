from params_guideline import Parser

parser = Parser(description='Process some integers.')
json_parser = parser.add_json_parser('--configs', default='configs.json', help='config json file')
json_parser.add_argument('test', type=int, help="test")
json_parser.add_argument('--test2', type=str, help="test")

json_parser = parser.add_yaml_parser('--yaml_config', default='configs.yaml', help='config yaml file')
json_parser.add_argument('isyaml', type=str, help="test")
json_parser.add_argument('--hello', type=str, help="test")

args = parser.parse_args()
print('fin:', args)
print('fin:', args.configs.test)
