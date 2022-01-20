from pg.core import pg

@pg.parsing()
@pg.arg("--test", default='bb', condition=lambda x: len(x) < 5)
@pg.arg("--test2", default="1,2,3", type=list)
@pg.arg("--bool2", default=True, type=bool)

@pg.json.parsing("--json",  default='example/configs.json')
@pg.arg("--json_test")

@pg.torch.parsing("--opts", default='example/configs.pt')
@pg.arg("--dict")
def main(args):
    if args.bool2:
        print('true!')
    else:
        print('false!')

    print(args.test)
    print(args.test2)
    print(args)
    print(args.json)
    print(args.json.json_test)

if __name__ == "__main__":
    main()