# CONSTANTS
DEF_RESOLUTION = (600,400)
DEF_EFFECT     = "none"
DEF_FRAMERATE  = 15

# delay between serving data to client 
TIME_STAMP     = 1


RED_ESCAPE     = u"\u001b[31m"
GREEN_ESCAPE   = u"\u001b[32m"
ESCAPE_END     = u"\u001b[0m"
WARNING_PREFIX = RED_ESCAPE + u"[!]" + ESCAPE_END
GOOD_PREFIX    = GREEN_ESCAPE + u"[*]" + ESCAPE_END