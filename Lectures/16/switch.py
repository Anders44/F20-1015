import simulated_system

class switch:

    def __init__ ( self, addr ):
        self.my_addr = addr
        self.state = 0                #  Assume that the switch is off
        simulated_system.system_set ( f"switch:{addr}", 0 )    # Set to off

    def isOn ( self ):
        if self.state == 0:
            return False
        else:
            return True

    def turnOn ( self ):
        self.state = 1    
        simulated_system.system_set ( f"switch:{addr}", 1 )    # Set to on

    def turnOff ( self ):
        self.state = 0    
        simulated_system.system_set ( f"switch:{addr}", 0 )    # Set to off
   

if __name__ == "__main__":
    print ( "In Main" )

    s = switch(4)
    print ( f"{s}" )
 
