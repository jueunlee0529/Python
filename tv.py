class TV :
    def __init__(self, power, channel, volume) :
        self.power = True
        self.channel = channel
        self.volume = volume

    def on_off(self) :
        if(self.power == True) :
            self.power = 0
            print("Turn Off")
        else:
            self.power = True
            print("Turn On")

    def info(self) :
        print("Power : ", self.power)
        print("Channel : ", self.channel)
        print("Volume : ", self.volume)
        
    def set_channel(self, n) :
        if(self.power == True) :
            self.channel = channel
        else :
            print("Power Off")

    def set_volume(self, n):
        if(self.volume == True) :
            self.volume = volume
        else :
            print("Power Off")

tv = TV("True", "1", "16")
tv.info()
tv.on_off()
tv.on_off()
