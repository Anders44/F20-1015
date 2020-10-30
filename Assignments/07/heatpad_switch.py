
import switch

class output_switch ( switch.switch ):

    def __init__ ( self ):
        self.my_addr = 6
        super().__init__ ( 6, "heatpad" )



if __name__ == "__main__":
    print ( "In Main" )

    s = output_switch()
    print ( f"{s}" )
 
