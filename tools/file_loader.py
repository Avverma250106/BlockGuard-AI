def load_contract(path):

    with open(path, "r") as f:
        code = f.read()

    return code