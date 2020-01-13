# https://app.codesignal.com/challenge/deMCqfKThepek7YMH
def lrc2subRip(lrcLyrics, songLength):
    sr = []
    hr = 0
    milli, sec, mn = parseTime(lrcLyrics[0], 7, 4, 1)
    milli *= 10
    if mn > 59:
        hr = mn // 60
        mn = mn % 60
    starttime = buildSubRip(hr, mn, sec, milli)

    for i in range(1, len(lrcLyrics)+1):
        if i == len(lrcLyrics):
            milli = 0
            sec, mn, hr = parseTime(songLength, 6, 3, 0)
            print(sec, mn, hr)
        else:
            milli, sec, mn = parseTime(lrcLyrics[i], 7, 4, 1)
            milli *= 10
            if mn > 59:
                hr = mn // 60
                mn = mn % 60
        endtime = buildSubRip(hr, mn, sec, milli)
        sr.append(str(i))
        sr.append(starttime + " --> " + endtime)
        text = ""
        if len(lrcLyrics[i-1]) > 11:
            text = lrcLyrics[i-1][11:]
        sr.append(text)
        if i < len(lrcLyrics):
            sr.append("")
        starttime = endtime

    return sr


def parseTime(s, a, b, c):
    x = int(s[a:a+2])
    y = int(s[b:b+2])
    z = int(s[c:c+2])
    return x, y, z


def buildSubRip(hr, mn, sec, milli):
    result = str(hr).rjust(2, '0')+':'
    result += str(mn).rjust(2, '0')+':'
    result += str(sec).rjust(2, '0')+','
    result += str(milli).rjust(3, '0')
    return result
