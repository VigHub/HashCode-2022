import pandas as pd
import numpy as np


class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


class Project:

    def __init__(self):
        pass



def read_file(file_name):
    contributors = {}
    projects = {}
    skill_set = {}
    
    C, P = 0,0
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        first_line = lines[0].split()
        line_index = 1
        C, P = map(int, first_line)
        tot = (10*C+1)
        contributors["skill"] = [np.nan]*tot
        for _ in range(C):
            contributor_name, n_skills = lines[line_index].split()
            n_skills = int(n_skills)
            line_index += 1
            skills = {}
            contributors[contributor_name] = [0]*tot
            for _ in range(n_skills):
                skill, level = lines[line_index].split()
                level = int(level)
                if skill not in skill_set:
                    skill_set[skill] = len(skill_set)
                    contributors["skill"][skill_set[skill]] = skill
                contributors[contributor_name][skill_set[skill]] = level
                skills[skill] = level
                line_index += 1
            
        df_cont = pd.DataFrame(contributors)
        df_cont = df_cont[df_cont["skill"].notnull()]
        df_cont.set_index("skill")
        # print(df_cont)
        

        for _ in range(P):
            line = lines[line_index].split()
            name = line[0]
            d, s, b, r = map(int, line[1:])
            projects[name]  = {"Day": d,"Score": s, "BestBD": b, "Skills":[]}
            line_index += 1
            for _ in range(r):
                skill, level_req = lines[line_index].split()
                level_req = int(level_req)
                line_index += 1
                projects[name]["Skills"].append((skill, level_req))
            
        df_proj = pd.DataFrame(projects).transpose()
        # print(df_proj)

    
    return df_cont, df_proj, skill_set
