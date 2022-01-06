from pg.core import pg

@pg.parsing()
@pg.arg("--test", condition=lambda x: len(x) < 5)
@pg.arg("--test2", default="1,2,3", type=list)

@pg.json.parsing("--json")
@pg.arg("--json_test")

@pg.torch.parsing("--opts", default='configs.pt')
@pg.arg("--dict")
def main(args):
    print(args.test)
    print(args.test2)
    print(args)
    print(args.json)
    print(args.json.json_test)

if __name__ == "__main__":
    main()