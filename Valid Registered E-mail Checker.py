import os
import requests
import time
import urllib3
import sys
from multiprocessing import Pool
def checksss(email):
    try:
        result = requests.get("https://www.elevenia.co.id/register/ValidEmailCheck/isValidEmailAjax.do?memID=" + email)
        kontol = result.text+" => "+ email
        print kontol
        return kontol
    except requests.exceptions.ConnectionError:
        pass
    except UnicodeDecodeError: 
        pass
    except TypeError:
        pass
    except KeyboardInterrupt:
        exit()
urllib3.disable_warnings()
mailist_file = sys.argv[1]
output = sys.argv[2]
live_payload = "touch "+output
live = open(output,"w+")
live_counter=0
break_counter=0
file = open(mailist_file, 'r')
email = file.readlines()

if __name__ == "__main__":
    p = Pool(processes=35)
    for line in p.map(checksss, [line.rstrip('\n') for line in open(mailist_file)]):
        try:
            if "Y" in line:
                asu = line.replace("Y => ","")
                live.write(asu+"\n")
            else:
                pass
        except requests.exceptions.ConnectionError:
            continue
        except UnicodeDecodeError: 
            pass
        except KeyboardInterrupt:
            exit()
        