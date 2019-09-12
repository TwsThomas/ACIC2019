from miwae_test_drago import run_main_test
from miwae_train_drago import run_main_train
from threadpoolctl import threadpool_limits

import argparse

# python3 main_script.py test low --cpu 10
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="train or test")
parser.add_argument("dim", help="low or high")
parser.add_argument("--cpu", help="cpu limits",
                    default=10, type=int)
args = parser.parse_args()

max_cpu = args.cpu
print('°'*20)
print('running main script with:')
print("folder=", args.folder)
print("dim=", args.dim)
print('max cpu=',max_cpu)

if args.folder == "train":
    for id in range(1,3201):
        print('* * '*10)
        print('Run main_train id:', id)
        print('* * '*10)
        run_main_train(id, dim=args.dim)

elif args.folder == "test":
    for id in range(1,9):
        print('* * '*10)
        print('Run main_test id:', id)
        print('* * '*10)
        run_main_test(id, dim=args.dim)

else:
    raise args.folder + " received, but should be train or test"