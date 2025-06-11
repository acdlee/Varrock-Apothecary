import questionary
from collections import namedtuple

# Object for clarity
Prompt = namedtuple('Prompt', ('category', 'config'))

# Configs for control options (navigating through the CLI shop)
configs = [
    {
      "category": "home",
      "configs": {
          "message": '''
          Welcome to the Varrock Apothecary!
          Please select a category to shop from:''',
          "choices": [
              "Herbs",
              "Ingredients",
              "Potions"
          ]
      }
    },
    {
        "category": "herbs",
        "configs": {
            "message": '''
            Welcome to our Herb collection.
            Please select a herb to purchase:''',
            "choices": ['1', '2', '3']
        }
    },
    {
        "category": "ingredients",
        "configs": {
            "message": '''
            Welcome to our Ingredient collection.
            Please select an ingredient to purchase:''',
            "choices": ['4', '5', '6']
        }
    },
    {
        "category": "potions",
        "configs": {
            "message": '''
            Welcome to our Potion collection.
            Please select a potion to purchase:''',
            "choices": ['7', '8', '9']
        }
    }
]

class ShopInterface:
    controls = [Prompt(config["category"], config['configs']) for config in configs]
    
    def __init__(self):
        self.run_interface()
        
    def run_interface(self):
        choice = 'home'
        while True:
            choice = choice.lower()
            match choice:
                case 'home':
                    choice = self.home()
                case 'herbs' | 'ingredients' | 'potions':
                    choice = self.open_shop_category(choice)
                case _:
                    break    
                    
    def home(self):
        control = self.controls[0]
        return questionary.select(
            control.config["message"],
            choices=control.config["choices"]
        ).ask()
        
    def open_shop_category(self, input_category):
        def determine_category(control):
            if control.category == input_category:
                return True
            return False
        
        control = list(filter(determine_category, self.controls))[0]
        # print(control)
        return questionary.select(
            control.config["message"],
            choices=control.config["choices"]
        ).ask()
        
if __name__ == "__main__":
    SI = ShopInterface()
    # def determine_category(control):
    #     if control.category == "herbs":
    #         return True
    #     return False
    
    # test = filter(determine_category, SI.controls)
    # print(list(test))