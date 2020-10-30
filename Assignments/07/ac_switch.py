
import switch

class ac_switch ( switch.switch ):

    def __init__ ( self ):
        self.my_addr = 5
        super().__init__ ( 5, "ac" )



if __name__ == "__main__":
    print ( "In Main" )

    s = ac_switch()
    print ( f"{s}" )
 
