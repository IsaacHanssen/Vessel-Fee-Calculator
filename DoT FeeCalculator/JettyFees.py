def Spacer():
    print("-----------------------------------------------------------------------------------------")

def CostJettyRecreational(length, days):
    Spacer()
    if length > 25:
        return length * 8.25 * days
    if length <= 25:
        return 58.85 * days
    
def CostJettyCommercial(length, days):
    Spacer()
    return length * 8.25 * days

def VesselShortTerm(length):
    Spacer()
    return length * 94.35

def JettyCalculation():
    Spacer()
    print("1) Use of Jetty/Wharf by Recreational Vessel")
    print("2) Use of Jetty/Wharf by Commercial Vessel ")
    print("3) Short-term use of a service Jetty/Wharf by any Vessel (12 Months Paid in Advance)")
    response = int(input("Which scenario best describes your situation? "))
    Spacer()
    length = int(input("How long is your vessel? "))
    Spacer()
    if response == 1 or response == 2:
        days = int(input("How many days will you use the Jetty/Wharf for? "))
        if response == 1:
            print(f"That will cost ${CostJettyRecreational(length, days)}")
        if response == 2:
            print(f"That will cost ${CostJettyCommercial(length, days)}")
    else:
        print(f"That will cost ${VesselShortTerm(length)}")