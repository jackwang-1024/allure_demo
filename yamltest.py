# import yaml

# class Yaml_Util:
#     def
#
# with open('./login.yaml',encoding='utf-8') as f:
#     ym = yaml.load(f,yaml.FullLoader)

# print(ym)
# print(ym[0].get("case_name"))
# print(ym[0].get("request").get("url"))
# print(ym[0].get('request').get('headers').get('Content-Type'))


import yaml


class YamlUtil:
    def __init__(self, yaml_path):
        '''
        初始化时 传入yaml文件路径
        :param yaml_file:
        '''
        self.yaml_path = yaml_path

    def yaml_read(self):
        '''
        yaml文件的读取
        '''
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            ym = yaml.load(f, Loader=yaml.FullLoader)
        return ym

if __name__ == '__main__':
    ym = YamlUtil('login.yaml').yaml_read()
    print(ym)