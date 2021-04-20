def putResultTogether(results, funcName):
    i = 0
    if(funcName == "CountingWords"):
        resultString = ""
        for res in results:
            resultString = resultString + res[0] + ": " + str(res[1]) +"\n"
            i+=res[1]
        resultString+= "Total: " + str(i) + "\n"
        return resultString
    if funcName == "WordCount":
        resultString = ""
        for res in results:
            resultString = resultString + res[0] + ": " + res[1] +"\n"
        return resultString