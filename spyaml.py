import yaml


if __name__ == '__main__':
    with open('storage.yaml') as yaml_file:
        print(yaml.load(yaml_file.read()))
