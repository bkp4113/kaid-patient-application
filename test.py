import pprint
from requests import Session, Request

test_apis = [ "http://127.0.1.1:1990/users?username=patelbb","http://127.0.1.1:1990/users?id=1","http://127.0.1.1:1990/roles?id=1",\
                "http://127.0.1.1:1990/roles?roles=admin","http://127.0.1.1:1990/roles?roles=user","http://127.0.1.1:1990/roles",\
                "http://127.0.1.1:1990/users","http://127.0.1.1:1990/paitent","http://127.0.1.1:1990/paitent?id=5",\
                "http://127.0.1.1:1990/paitent?first_name=Tom","http://127.0.1.1:1990/paitent?first_name=Catherine&gender=Female&id=6",\
                "http://127.0.1.1:1990/paitent?first_name=Jennifer&middle_name=Tom&last_name=Patelgender=Female&dob=03/25/2020"]

request_api = {
    "GET" : [test_apis[0], test_apis[1], test_apis[9], test_apis[3],test_apis[4], test_apis[4],test_apis[5], test_apis[6], test_apis[8], test_apis[9]],
    #"POST" : [test_apis[11]],
    #"PUT" : [test_apis[10], test_apis[0], test_apis[0], test_apis[0],test_apis[0], test_apis[0],test_apis[0], test_apis[0]],
    #"DELETE" : [test_apis[5]]
}

s = Session()

for r in request_api:

    for api in request_api[r]:
        request = Request(method=r, url=api)
        prep = request.prepare()
        response = s.send(prep)
        pprint.pprint(api)
        pprint.pprint(response.status_code)
        pprint.pprint(response.text)

        print("\n\n")