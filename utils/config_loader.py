from pathlib import Path
import os
import yaml

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    return config

# utils/config_loader.py

# def _project_root()-> Path:
#     return Path(__file__).resolve().parents[1]

# def load_config(config_path: str | None=None) -> dict:
#     """
#     Resolve config path reliably irrespective of CWD.
#     Priority: explicit arg > CONFIG_PATH env > <project_root>/config/config.yaml
#     """
#     env_path=os.getenv("CONFIG_PATH")
#     print('env_path',env_path)
#     if config_path is None:
#         # print('str(_project_root() / "config" / "config.yaml")',str(_project_root() / "config" / "config.yaml"))
#         config_path=env_path or str(_project_root() / "config" / "config.yaml")
#         # print('config_path',config_path)

#     path=Path(config_path)

#     print('path',path)

#     if not path.is_absolute():
#         path=_project_root() / path

#     if not path.exists():
#         raise FileNotFoundError(f"Config file not found: {path}") 

#     with open(path ,"r",encoding="utf-8") as f:
#         return yaml.safe_load(f) or {}  

# print(load_config(config_path="config/config.yaml") )    
# print(load_config() ) 
# print(load_config()) 