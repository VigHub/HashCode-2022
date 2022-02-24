from calculate_score import calculate_score
from read_file import read_file
from run_algo import run_algo
from write_file import write_file


if __name__ == '__main__':
    files = ['a', 'b', 'c', 'd', 'e', 'f']
    # files = ['b']
    for f in files:
        input_file = f'inputs/{f}.txt'
        output_file = f'outputs/{f}.txt'
        score_file = f'scores/{f}.txt'
        try:
            df_cont, df_proj, skill_set = read_file(input_file)
        except FileNotFoundError:
            continue
        except KeyboardInterrupt:
            pass
        doable_projects = run_algo(df_cont, df_proj, skill_set)
        # score = calculate_score(pizza, clients)
        # print(f'{f = } {score = }')
        write_file(output_file, doable_projects)
