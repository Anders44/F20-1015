
"""
    Simulated system
"""
mem = {}
def system_set ( tag, value ):
    mem[tag] = value
    return

def system_init ( m ):
    mem = m

def get_state():
    return mem
