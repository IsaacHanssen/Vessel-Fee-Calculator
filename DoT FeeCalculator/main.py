from VesselAccomodationFees import *
from JettyFees import *
from MooringFees import *

def main():
    Spacer()
    print("What would you like to calculate?")
    print("1) Vessel Accommodation Fees")
    print("2) Jetty Fees")
    print("3) Mooring Fees")
    print("4) to be implemented...")
    response = int(input("Respond here: "))
    if response == 1:
        VesselAccomodationFee()
        Spacer()
    if response == 2:
        JettyCalculation()
        Spacer()
    if response == 3:
        MooringFee()
        Spacer()


main()