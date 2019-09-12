from miwae_test_drago import run_main_test

# import argparse

# # python3 main_script.py test low 
# # taskset -c 44-87 python3 main_script.py train low 
# parser = argparse.ArgumentParser()
# parser.add_argument("folder", help="train or test")
# parser.add_argument("dim", help="low or high")
# parser.add_argument("--cpu", help="cpu limits",
#                     default=10, type=int)
# args = parser.parse_args()

# max_cpu = args.cpu
# print('°'*20)
# print('running main script with:')
# print("folder=", args.folder)
# print("dim=", args.dim)
# print('max cpu=',max_cpu)


dim = "low"
d=10
h=128
add_mask=False
num_samples_zmul=50
num_samples_xmul=50
perc_miss = 0.1
folder = "test"

in_folder = "data/TestDatasets_"+dim+"D/"
out_folder = "data/TestDatasets_"+dim+"D/results/"


for d in range(10,20,30): 

    for id_data in range(1,9):
        print('* * '*10)
        print('Run main_test id:', id_data)
        print('* * '*10)
        run_main_test(id_data, dim , d, h, add_mask,
                    num_samples_zmul, num_samples_xmul, perc_miss,
                    in_folder, out_folder, folder)

# for id in range(1,3201):
#         print('* * '*10)
#         print('Run main_train id:', id)
#         print('* * '*10)
#         run_main_train(id, dim=args.dim)
