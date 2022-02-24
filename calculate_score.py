
def calculate_score(pizza, clients):
    score = 0
    for client in clients:
        ok = True
        for like in client.likes:
            if like not in pizza:
                ok = False
                break
        if not ok:
            continue
        for dislike in client.dislikes:
            if dislike in pizza:
                ok = False
                break
        if ok:
            score += 1
    return score
