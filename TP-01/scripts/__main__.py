import json
from json.tool import main
from traceback import print_tb
from jinja2 import Template, Environment, FileSystemLoader

def load_json_data_from_file(file_path):
    try:   
        f = open(file_path) # Opening JSON file

    except:
        print("")
        print("** Erreur File_Path **")
        print("")

    data = json.load(f) # returns JSON object as a dict
    return data


def load_yaml_data_from_file(file_path):
    """
        A compléter ....
    """
    pass


def render_network_config(template_name, data):
    return template_name.render(data)
    

def save_built_config(file_name, data):
    try:
        File_object = open(file_name, "r+")
        File_object.write(data)
        File_object.close()
    except:
        print("Erreur dans l'écriture et/ou la sauvegarde des conf")    
    pass


if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader("templates"))

    templateESW2 = env.get_template("ESW2.j2")
    JsonLoadedESW2= load_json_data_from_file('/home/cpe/workspace/TP-01/data/ESW2.json') 
    dataESW2 = render_network_config(templateESW2,JsonLoadedESW2)  
    print("** Début conf ESW2 **")  
    print(" ")  
    print(dataESW2) 
    print("** Fin conf ESW2 **")  
    print(" ")
    save_built_config("/home/cpe/workspace/TP-01/config/ESW2.conf",dataESW2) 

    templateR2 = env.get_template("R2.j2")
    JsonLoadedR2= load_json_data_from_file('/home/cpe/workspace/TP-01/data/R2.json') 
    dataR2 = render_network_config(templateR2,JsonLoadedR2)
    print("** Début conf R2 **")  
    print(" ")
    print(dataR2)
    print("** Fin conf R2 **")
    save_built_config("/home/cpe/workspace/TP-01/config/R2.conf",dataR2) 

    pass

