import re
import numpy as np


def is_tachycardic(string):
    string = string.lower()
    if "tachycardic" in string:
        other_string = string.replace("tachycardic", "")
        if (re.search('[a-z]', other_string)):
            return False
        else:
            return True
    else:
        if len(string) == len("tachycardic"):
            zipped_string = zip(string, "tachycardic")
            count = 0
            for i, j in zipped_string:
                if i == j:
                    count = count
                else:
                    count += 1
            if count <= 2:
                return True
            else:
                return False

        elif len(string) == len("tachycardic")-1:
            counts = np.zeros(11)
            for ii in range(0, 11):
                mistakes = 0
                new_string = string[:ii] + '*' + string[ii:]
                zipped_string = zip(new_string, "tachycardic")
                for k, j in zipped_string:
                    if k == j:
                        mistakes = mistakes
                    else:
                        mistakes += 1
                counts[ii] = mistakes
                new_string = string
            if min(counts) <= 2:
                return True
            else:
                return False

        elif len(string) == len("tachycardic")-2:
            counts = np.zeros(66)
            kk = 0
            for ii in range(0, 11):
                mistakes = 0
                new_string = string[:ii] + '*' + string[ii:]
                for jj in range(ii+1, 12):
                    second_new_string = new_string[:jj] + '*' + new_string[jj:]

                    zipped_string = zip(second_new_string, "tachycardic")
                    for k, j in zipped_string:
                        if k == j:
                            mistakes = mistakes
                        else:
                            mistakes += 1
                    counts[kk] = mistakes
                    kk = kk + 1
                    second_new_string = new_string
                new_string = string
            if min(counts) <= 2:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    is_tachycardic()
