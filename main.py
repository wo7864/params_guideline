from src.core import pg

@pg.parsing()
@pg.arg("--test", condition=lambda x: len(x) < 5)
@pg.arg("--test2", default='test', type=str)

@pg.json.parsing("--json")
@pg.arg("--json_test")

@pg.torch.parsing("--opts")
@pg.arg("--dict")
def main(args):
    print(args.opts.dict)

if __name__ == "__main__":
    main()