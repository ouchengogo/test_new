import configparser

def read_config(file_path):
    cf = configparser.ConfigParser()
    cf.read(file_path)
    section = cf["Test"]
    for key in section:
        print(key, ":", section[key])

read_config(r"C:\Users\ouchen\Learn_on_road\jiekou_sample\daming\cfg.ini")