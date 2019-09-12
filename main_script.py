from miwae_test_drago import run_main_test
from miwae_train_drago import run_main_train
from threadpoolctl import threadpool_limits

import argparse

print('Hello')
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="train or test")
parser.add_argument("dim", help="low or high")
args = parser.parse_args()
# print(args.dim)

print("folder=", args.folder)
print("dim=", args.dim)

if args.folder == "train":
    for id in range(1,3201):
        print('* * '*10)
        print('Run main_train id:', id)
        print('* * '*10)
        with threadpool_limits(limits=10):
            run_main_train(id)

elif args.folder == "test":
    for id in range(1,9):
        print('* * '*10)
        print('Run main_test id:', id)
        print('* * '*10)
        with threadpool_limits(limits=10):
            run_main_test(id)

else:
    raise args.folder + " received, but should be train or test"