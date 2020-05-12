import importlib
import pip 

def install_and_import(package):
    print("importing "+str(package)) 
    pkg=package.split("==")[0] 
    try:
        importlib.import_module(pkg)
    except ImportError:
        pip.main(['install', package])
    finally:
        globals()[pkg] = importlib.import_module(pkg)
        
def import_requirements():
    with open("requirements.txt",'r') as req :
        for line in req:
            install_and_import(line)
