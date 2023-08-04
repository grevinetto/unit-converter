import importlib.util
from pathlib import Path

class Caller:
    def __init__(self):
        self.data_folder = Path("../data")
        self.categories = self.get_available_categories()
       
    def get_available_categories(self):
        categs = [file.stem for file in self.data_folder.glob("*.py")]
        # Remove underscores from the python script names and capitalize each word for better presentation
        categs = [categ.replace("_", " ").title() for categ in categs]
        return sorted(categs)
        
    def call_dictionary(self, category):
        if category in self.categories:
            # Add underscores and change python script names to lowercase so they can be loaded as modules
            category = category.lower().replace(" ", "_")
            module_name = f"data.{category}"
            module_spec = importlib.util.spec_from_file_location(module_name, self.data_folder / f"{category}.py")
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            return module.conversion_data
        else:
            return None

if __name__ == "__main__":
    pass