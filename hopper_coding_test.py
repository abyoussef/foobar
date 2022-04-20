#// A valid IP address is any non-negative integer that is less than or equal to some maxIp.
#// An IP range is a pair of valid IP addresses that are inclusive bounds to a set of valid IP addresses.
#// Given an input of a maxIp and a list of IP ranges, write a function that returns the minimum
#// valid IP address that is not contained in any of the input IP ranges.
#// Example
#// Input: maxIp = 8, blockedRanges = [(4-6), (0-2), (8-8)]
#//
#// Output: 3

#// Input: maxIp = 7, blockedRanges = [(4-7), (0-3), (8-8)] => ?
# [(0-6), (2-4), (8,8)] => 
from typing import Dict, List, Tuple


# return a non-negative integer that is less than maxIP and not in blockedRanges
# maxIP: int = Non-negative maximum value for IP address
# blockedRanges: List[Tuple[int,int]] = a list of valid IP Ranges
def minValidIP(maxIP:int, blockedRanges : List[Tuple[int,int]]) -> int:
    try:
        if maxIP == 0:
            return 0
        # Dictionary to store IP ranges by unique first element. Overlapping tolerated.
        dictRanges : Dict[int, int] = dict()
        for ipMin,ipMax in blockedRanges:
            if ipMin > maxIP:
                continue
            if ipMin in dictRanges:
                dictRanges[ipMin] = min(max(ipMax, dictRanges[ipMin]), maxIP)
            else:
                dictRanges[ipMin] = min(ipMax, maxIP)
        # Check if dict is not empty, in which case return 0
        if not dictRanges:
            return 0

        # sort IPranges by keys after transforming dict into item pairs
        sortedUniqueIPRanges:List[Tuple[int,int]] = sorted(dictRanges.items())

        validIp = 0
        for ipMin,ipMax in sortedUniqueIPRanges:
            if validIp < ipMin:
                break
            if validIp > ipMax:
                continue
            validIp = ipMax + 1
        
        if validIp <= maxIP:
            return validIp
        else:
            raise Exception("Can not find a minimum valid IP address")
    except Exception as e: print(e)


if __name__ == "__main__":
    # Test cases
    print("return 3: ", minValidIP(8, [(4,6), (0,2), (8,8)]))
    print("return 7: ", minValidIP(8, [(0,6), (2,4), (8,8)]))
    print("Raise Error and return None: ", minValidIP(8, [(0,7), (2,4), (8,8)]))