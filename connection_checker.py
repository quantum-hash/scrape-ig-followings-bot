import requests, random, os, time


def check(url = "https://www.amazon.com", frequency = [240,300]):
    """
    

    Parameters
    ----------
    url : str
        DESCRIPTION. The default is "https://www.amazon.com".
    frequency : list
        DESCRIPTION. The default is [240,300].

    Returns
    -------
    None.

    """
    print("\n"+'---------- ' + 'WELCOME ' + os.getlogin() +' ----------'+ '\n')
    num = False
    counter = 0
    while num == False:
        try:
            requests.get(url, timeout=5)
            num = True
        except (requests.ConnectionError, requests.Timeout) as exception:
            counter += 1
            wait = random.randint(frequency[0], frequency[1])
            #wait = random.randint(2,3)
            print('no internet connection, retrying in '+ str(wait)+' s or also in '+ str(round((wait/60),2))+" m ("+str(counter)+") \n")
            time.sleep(wait)
            pass

    if counter == 0:
        print ('the connection is working fine !'+'\n')
    elif counter == 1:
        print ('only one retry to get the connection back !'+'\n')
    else:
        print (str(counter) + ' retries to finally get the connection back !'+'\n')


# import connection_checker
# connection_checker.check(url = "https://www.amazon.com", frequency = [10,300])