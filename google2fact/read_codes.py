""" read backup codes from default google cloud and generate file """
import os


codes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "codes")
codes_file = os.environ("GMAIL_CODES")
codes_clean_file = os.path.join(codes_path, 'normalized.txt')


if not os.path.isfile(codes_file):
    codes = []
    with open(codes_file, "r") as sf:
        for line in sf.readlines():
            if ". " in line:
                one_num, second_num = line.split('. ')[1:]
                one_num = one_num.split("\t\t")[0]+"\n"
                codes += one_num + second_num
    with open(codes_file, "w+") as cf:
        cf.writelines(codes)


def get_code():
    """ return code from codes.txt and """
    codes = []
    with open(codes_file, "r") as cf:
        for num, line in enumerate(cf.readlines()):
            if num == 1:
                if line.startswith("Need"):
                    raise Exception(line)
            codes.append(line)
    code = codes[0]
    codes.pop(0)

    with open(codes_file, "w+") as cf:
        if len(codes) > 0:
            cf.writelines(codes)
        else:
            cf.write("Need new codes")
    return code

