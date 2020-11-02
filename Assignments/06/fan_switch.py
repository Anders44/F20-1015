
import switch

class fan_switch ( switch.switch ):

    def __init__ ( self ):
        self.my_addr = 3
        super().__init__ ( 3, "fan" )



if __name__ == "__main__":
    print ( "In Main/Fan" )

    s = fan_switch()
    print ( f"{s}" )
 
