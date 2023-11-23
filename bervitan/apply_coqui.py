from os import chdir, system
from sys import argv
from re import sub

coqui_path = argv[1]
absolute_input_filepath = argv[2]
index_path = argv[3]
f0method = argv[4]
absolutile_output_filepath = argv[5]
model_name = argv[6]
coqui_is_half = argv[7]
f0up_key = argv[8]

def run(run_debug: bool = False): 
    chdir(coqui_path)
    command = f"runtime\python.exe tools\infer_cli.py \
        --input_path {absolute_input_filepath} \
        --index_path {index_path} \
        --f0method {f0method} \
        --opt_path {absolutile_output_filepath} \
        --model_name {model_name} \
        --is_half {coqui_is_half} \
        --f0up_key {f0up_key} \
        "
    command = sub(' +', ' ', command)
    if run_debug:
        print(command)
    exit_code = system(command)
    return exit_code

exit_code = run(True)
exit(exit_code)