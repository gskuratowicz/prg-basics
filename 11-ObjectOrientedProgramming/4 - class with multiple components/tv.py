# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.available_channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self,*channels_list):
        self.available_channels.extend(channels_list)

    def show_channels(self):
        if self.available_channels == []:
            print("No available channels.")
        else:
            print("Channel list:")
            i = 1
            for element in self.available_channels:
                print(f"{i}. {element}")
                i += 1

    def show_status(self):
        if self.is_on:
            if self.channel_no > len(self.available_channels):
                print("Channel does not exist.")
            else: 
                print(f"TV is turned on; current channel is {self.channel_no} ({self.available_channels[self.channel_no - 1]}). Volume is set to {self.volume}")
        elif not self.is_on:
            print("TV is turned off.")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    
    def decrease_volume(self):
            if self.volume > 0:
                self.volume -= 1