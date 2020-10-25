
import switch

class charger_switch ( switch.switch ):

    def __init__ ( self ):
        self.my_addr = 1
        super().__init__ ( 1, "charger" )



if __name__ == "__main__":
    print ( "In Main" )

    s = charger_switch()
    print ( f"{s}" )
 
