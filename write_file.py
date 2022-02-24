
def write_file(out_file, score_file, score, pizza):
    previous_score = 0
    try:
        with open(score_file, 'r') as sf:
            previous_score = int(sf.readline())
    except FileNotFoundError:
        pass
    # if score is less than previuos, 
    # do not write to file and return
    if score < previous_score:
        return
    # now write to file 
    with open(score_file, 'w') as sf:
        sf.write(str(score))
    with open(out_file, 'w') as of:
        of.writelines(f'{len(pizza)} {" ".join(pizza)}')
    