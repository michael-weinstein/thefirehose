def countServerErrors(statusCodes:list):
    errorCount = 0
    for code in statusCodes:
        if code // 100 == 5:
            errorCount += 1
    return errorCount / len(statusCodes)

def singleAlarm(submitter):
    from . import appliances
    count = 0
    statusCounts = {}
    try:
        while True:
            strawman = appliances.Strawman()
            response = submitter(strawman)
            count += 1
            status = response.status_code
            if not status in statusCounts:
                statusCounts[status] = 0
            statusCounts[status] += 1
            print("Submitted: %s\tStatus: %s\t%s\t%s%s" % (count, status, strawman.email, strawman.password, " "*40), end="\r")
    except KeyboardInterrupt:
        print()
        print(statusCounts)
    quit()

def multiAlarm(submitter, attackBlockSize:int = 1000, sleepTime:int = 3, maxErrorRatio:float = 0.2):
    from . import easyMultiprocessing
    from . import appliances
    import time
    totalCounts = 0
    statusCounts = {}
    try:
        while True:
            userInfoList = []
            for i in range(attackBlockSize):
                userInfoList.append(appliances.Strawman())
            results = easyMultiprocessing.easyMultiprocessing.parallelProcessRunner(submitter, userInfoList)
            responseCodes = [response.status_code for response in results]
            errorPercent = countServerErrors(responseCodes)
            totalCounts += len(responseCodes)
            for responseCode in responseCodes:
                if not responseCode in statusCounts:
                    statusCounts[responseCode] = 0
                statusCounts[responseCode] += 1
            print("%s submissions %s" %(totalCounts, statusCounts), end = "\r")
            if errorPercent > maxErrorRatio:
                break
            time.sleep(sleepTime)
    except KeyboardInterrupt:
        pass
    print(statusCounts)
    quit()