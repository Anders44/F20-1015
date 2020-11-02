
import switch

class heater_switch ( switch.switch ):

    def __init__ ( self ):
        self.my_addr = 4
        super().__init__ ( 4, "heater" )



if __name__ == "__main__":
    print ( "In Main" )

    s = heater_switch()
    print ( f"{s}" )
 
