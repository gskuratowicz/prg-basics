class Phone():
    def __init__(self,model,year,storage):
        self.model = model
        self.year = year
        self.storage = storage
        self.is_flashlight = False
    
    def flashlight_on(self):
        self.is_flashlight = True

    def flashlight_off(self):
        self.is_flashlight = False

    def display_info(self):
        print("Information about phone:")
        print(f"Model name: {self.model}")
        print(f"Release year: {self.year}")
        print(f"Storage space: {self.storage}GB")
        if self.is_flashlight == True:
            print("The flashlight is turned on.")
        elif self.is_flashlight == False:
            print("The flashlight is turned off.")

phone1 = Phone("iPhone 12 Mini",2012,128)
phone1.flashlight_on()
phone1.display_info()