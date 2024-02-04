# This python code will follow a list of configurations provided by the user
# The configurations will be provided by a HCl/JSON file in the following format defined
# This code will perform transformations based on the 
# functions set up in the files here 
from importlib.machinery import SourceFileLoader

def transform(msg,module_name, file_path) -> str:
    # Choose a unique module name
    user_module = SourceFileLoader(module_name, file_path).load_module()
    result = getattr(user_module, "decodebase64")(msg)
    return result