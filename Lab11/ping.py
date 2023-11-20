'''function'''
def ping():
    '''solution'''
    web_ping = input()
    input()
    pinging = input()
    line1 = input().replace("<1", "=0")
    line2 = input().replace("<1", "=0")
    line3 = input().replace("<1", "=0")
    line4 = input().replace("<1", "=0")
    ip_add = ""
    if not web_ping[web_ping.find("ping ") + 5][0].isdigit():
        front = pinging.find("[")
        back = pinging.find("]")
        ip_add = pinging[front + 1:back]
    else:
        ip_add = web_ping[web_ping.find("ping ") + 5:]
    receive = (line1 + line2 + line3 + line4).count(ip_add)
    print("Ping statistics for %s:" % (ip_add))
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s)," %
          (receive, 4 - receive, str((4 - receive) * 25) + "% loss"))
    time = [calculatetime(line1), calculatetime(line2), \
            calculatetime(line3), calculatetime(line4)]

    for _ in range(time.count("Not have")):
        time.remove("Not have")

    if len(time):
        minimum = min(time)
        maximum = max(time)
        average = int(sum(time) / len(time))
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" \
              % (minimum, maximum, average))

def calculatetime(line):
    '''calculate time'''
    if line.count("time="):
        start = line.find("time=")
        stop = line.find("ms")
        return int(line[start + 5:stop])
    return "Not have"

ping()
