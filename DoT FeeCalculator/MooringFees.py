from JettyFees import Spacer

def AnnualLicenceFees():
    recMoorExcl = 677.35
    recMoorShare = 349.0
    latePayment = 120.85
    sharedUseAuth = 108.45
    generalMoor = 872.5
    Spacer()    
    print("1) Exclusive-Use Annual License for Recreational Mooring Site")
    print("2) Shared-Use Annual License for Recreational Mooring Site")
    print("3) Annual Mooring License for Commercial General Mooring Site")
    response = int(input("Which response best suites your needs? "))
    Spacer()
    late = input("Are you paying your license late? y/n ")
    if late == "n":
        latePayment = 0
    if response == 1:
        return recMoorExcl + latePayment
    if response == 2:
        return recMoorShare + latePayment + sharedUseAuth
    if response == 3:
        return generalMoor + latePayment

def ApplicationFees():
    Spacer()
    mooringLic = 120.85
    subLicVessel = 120.85
    registerAdditionalVessel = 120.85
    excRegMoor = 120.85
    return 120.85 # All the same fee

def CommercialLicenseFees():
    Spacer()
    return 2836.30

def MooringFee():
    Spacer()
    print("1) Annual License fees - Mooring Regulations 1998")
    print("2) Application Fees")
    print("3) Annual Commercial Mooring Fees (resources site)")
    response = int(input("What service are you looking for? "))
    if response == 1:
        return print(f"That will cost ${AnnualLicenceFees()}")
    if response == 2:
        return print(f"All Applications cost ${ApplicationFees()} inclusive of application for a licence, substitution of a licensed vessel, registering an additional vessel or exchange of registered mooring sites")
    if response == 3:
        return print(f"That will cost ${CommercialLicenseFees()} Annually")