from calculate_score import calculate_score
from random import sample
import pandas as pd

def run_algo(df_cont: pd.DataFrame, df_proj:pd.DataFrame, skill_set):
    df_cont = df_cont.set_index("skill")
    doable_projects = {}
    deleted_people = {}
    for p_name, p_info in df_proj.iterrows():
        for s_name, s_value in p_info["Skills"]:
            d = df_cont.iloc[skill_set[s_name]]
            cont_names = d[d >= s_value].sort_values(axis=0)
            if len(cont_names) > 0:
                if not p_name in doable_projects:
                    doable_projects[p_name] = {"People": []}
                    deleted_people[p_name] = []
                person_name = cont_names.keys()[0]
                doable_projects[p_name]["People"].append(person_name)
                # remove p from matrix
                deleted_people[p_name].append(df_cont[person_name])
                del df_cont[person_name]
            else:
                if p_name in doable_projects:
                    for p in deleted_people[p_name]:
                        # reinsert p in matrix
                        df_cont[p.name] = p
                    del doable_projects[p_name]
                break

        if p_name in doable_projects and len(p_info["Skills"]) != len(doable_projects[p_name]["People"]):
            for p in deleted_people[p_name]:
                # reinsert p in matrix
                df_cont[p.name] = p
            del doable_projects[p_name]
            
    return doable_projects
