def time_planner(dur, time_A, time_B):
    """Problem: Return the time slot where a meeting can be scheduled between persons A and B for the required duration
        Space Complexity: O(1)
        Time Complexity: O(nlogn + mlogm) for non-sorted arrays, where n and m are lengths of timesA and timesB.

        # Case 1 - overlap exists which is less than equal to the duration
        # time_A = [[24th april, 2017, 10.00 am , 24th april, 2017, 12.00 pm], [24th april, 2017, 12.00 pm, 24th april, 2017, 12.30 pm], [24th april, 2017, 8.30 am, 24th april, 2017, 9.00 am]]
        # time_B = [[24th april, 2017, 9.00 am, 24th april, 2017, 10.00 am], [23rd april, 2017, 10.00 am, 23rd april, 2017, 10.30 am], [24th april, 2017, 11.00 am, 24th april, 2017, 1.00 pm], [24th april, 2017, 3.00 pm, 24th april, 2017, 4.00 pm]]

        >>> time_A = [[1493028000, 1493035200], [1493035200, 1493037000], [1493022600, 1493024400]] 
        >>> time_B = [[1493024400, 1493028000], [1492941600, 1492943400], [1493031600, 1493038800], [1493046000, 1493049600]] 
        >>> dur = 3600

        # output is 11.00 am to 12.00 pm 
        >>> print time_planner(dur, time_A, time_B)
        [1493031600, 1493035200]


        # Case 2 - No overlap exists 
        >>> time_A = [[1493020800, 1493024400], [1493024400, 1493026200]] 
        >>> time_B = [[1493031600, 1493035200]] 
        >>> dur = 3600
        >>> print time_planner(dur, time_A, time_B)
        []


        # Case 3 - Overlap is less than duration
        >>> time_A = [[1493020800, 1493024400], [1493024400, 1493026200]]
        >>> time_B = [[1493020800, 1493021700]]
        >>> dur = 1800
        >>> print time_planner(dur, time_A, time_B)
        []

    """

    i = 0
    j = 0

    time_A.sort(key=lambda x: x[0])
    time_B.sort(key=lambda x: x[0])

    while i < len(time_A) and j < len(time_B):
        start_time = max(time_A[i][0], time_B[j][0])
        end_time = min(time_A[i][1], time_B[j][1])

        if start_time + dur <= end_time:
            return [start_time, start_time + dur]

        else:
            if time_A[i][1] < time_B[j][1]:
                i += 1
            else:
                j += 1

    return [] 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. Good WORK!"
    print    

