from calculate_score import calculate_score
from read_file import read_file
from run_algo import run_algo
from write_file import write_file
    


if __name__ == '__main__':
    files = ['a', 'b', 'c', 'd', 'e']
    for f in files:
        input_file = f'inputs/{f}.txt'
        output_file = f'outputs/{f}.txt'
        score_file = f'scores/{f}.txt'
        try:
            clients, ingredients_map = read_file(input_file)
        except FileNotFoundError:
            continue
        except Exception as e:
            break
        except KeyboardInterrupt: 
            pass
        pizza = run_algo(clients, ingredients_map)
        score = calculate_score(pizza, clients)
        print(f'{f = } {score = }')
        write_file(output_file, score_file, score, pizza)