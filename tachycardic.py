def is_tachycardic(string):
    string = string.lower()
    if "tachycardic" in string:
        return True
    else:
        return False

if __name__ == "__main__":
    is_tachycardic()
