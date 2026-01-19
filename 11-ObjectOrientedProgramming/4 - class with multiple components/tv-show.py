# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   tvset1 = TV()

   # object usage
   tvset1.set_channels("TVP1","TVP2","Polsat","TVN")
   tvset1.turn_on()
   tvset1.show_status()

   tvset1.set_channel(4)
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.show_status()

   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.increase_volume()
   tvset1.decrease_volume()
   
   tvset1.show_status()

    



if __name__ == "__main__":
   main() 