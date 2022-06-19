import os

import re


# Enter your code here 

sample_text=['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',

 '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',

 'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',

 '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',

 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',

 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',

 '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',

 'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',

 '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',

 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',

 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786']

listToStr = ' '.join([str(elem) for elem in sample_text])

 

def func1():

    r = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z-0-9]+)'

    kal = re.findall(r, listToStr)

    hosts= list()

    for i in kal:

        hosts.append(i)

    print(hosts)


def func2():

    m = r'(\d\d/[A-z]{3}/\d{4}:\d\d:\d\d:\d\d\s-\d{4})'

    gal = re.findall(m, listToStr)

    timestamps= list()

    for i in gal:

        timestamps.append(i)

    print(timestamps)

    

def func3():

    q = r'GET\s/[a-zA-Z0-9]*/*[a-zA-Z-.0-9]*/*[A-Za-z0-9-]*/*[A-Za-z0-9.-]*\s*[A-Za-z]*/[0-9.]*'

    zal = re.findall(q, listToStr)

    gfl = list()

    for i in zal:

        gfl.append(i)

    method_uri_protocol=[]

    for j in gfl:

        k = j.split()

        sal = tuple(k)

        method_uri_protocol.append(sal)

    print(method_uri_protocol)


def func4():

    h = r'(?:200|304|404)'

    hal = re.findall(h, listToStr)

    status= list()

    for i in hal:

        status.append(i)

    print(status)


def func5():

    p=r'(?:200|304|404)\s(\d+)'

    yal = re.findall(p, listToStr)

    content_size= list()

    for i in yal:

        content_size.append(i)

    print(content_size)

    '''For testing the code, no input is to be provided'''


if __name__ == "__main__":

    func1()

    func2()

    func3()

    func4()

    func5()