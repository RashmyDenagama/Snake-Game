# utils.py

def check_collision(pos1, pos2):
    return pos1 == pos2

def check_self_collision(head, body):
    return head in body[1:]
