from datetime import time
port = 7000
server = '10.0.1.123'

# Runtime settings

# Brightness in percent - eg. 70
#
schedule = {
    1: {
        '1500': 70,
        '1930': 40,
        '0330': 0
    },
    2: {
        '1500': 70,
        '1930': 40,
        '0330': 0
    },
    3: {
        '1500': 70,
        '1930': 40,
        '0330': 0
    },
    4: {
        '1500': 70,
        '1930': 40,
        '0330': 0
    },
    5: {
        '1500': 70,
        '1930': 40,
        '0330': 0
    },
    6: {
        '0330': 0
    }
}

# add excluded days
# 0 = monday
# 1 = tuesday
# 2 = wednesday
# 3 = thursday
# 4 = friday
# 5 = saturday
# 6 = sunday
exclusions = [0]
