import simulated_system

class switch:

    def __init__ ( self, addr, name ):
        self.my_addr = addr
        self.name = name
        self.state = 0                #  Assume that the switch is off
        simulated_system.system_set ( f"switch:{self.my_addr}", 0 )    # Set to off

    def isOn ( self ):
        if self.state == 0:
            return False
        else:
            return True

    def turnOn ( self ):
        self.state = 1    
        simulated_system.system_set ( f"switch:{self.my_addr}", 1 )    # Set to on

    def turnOff ( self ):
        self.state = 0    
        simulated_system.system_set ( f"switch:{self.my_addr}", 0 )    # Set to off

    def __str__ ( self ):
        if self.isOn():
            return f"Switch {self.name} at {self.my_addr} is ON"
        return f"Switch {self.name} at {self.my_addr} is off"

    def myName( self ) :
        return self.name



if __name__ == "__main__":
    print ( "In Main" )

    s = switch(4)
    print ( f"{s}" )
 
