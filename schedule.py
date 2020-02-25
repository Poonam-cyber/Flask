my_final_json_data={}
from datetime import *
from json import *
from operator import *
inputdata = ["Profile name :", "Start Date:", "End Date:"]
dictdata = {}
num = 1
dic={}
temp =[]
flag=0
view={}

def all_operations(user,profile_name,Start_date1,End_date1):
    for x in range(num):
        p = user
        size = 1
        inside_data = []
        for d in range(size):
            data = {}
            profile = profile_name
            Start_date =Start_date1
            End_date = End_date1
            new_SD = datetime.strptime(Start_date, "%d-%m-%Y").date()
            new_ED = datetime.strptime(End_date, "%d-%m-%Y").date()
            str_sd=new_SD.strftime("%d-%m-%Y")
            str_ed=new_ED.strftime("%d-%m-%Y")
            if new_SD>new_ED:
                print("Please Enter Valid Date")
                break
            else:
                with open("dictionary_list.json") as f:
                    load_data = load(f)
                try:
                    for key, value in load_data.items():
                        flag = 0
                        temp=list(load_data.keys())
                        if p in temp:
                            for x in load_data[p]:
                                old_ed = datetime.strptime(x["End Date:"], "%d-%m-%Y").date()
                                old_sd = datetime.strptime(x["Start Date:"], "%d-%m-%Y").date()
                                append_json_data = x
                                inside_data.append(append_json_data)
                                print("before",inside_data)
                                print("old sd:",old_sd,"new sd:",new_SD,"old ed :",old_ed,"new ed:",new_ED)
                                if new_ED<old_sd:
                                    print("break : old sd ",old_sd,"newed", new_ED )
                                    break
                                if x["Profile name :"]==profile:
                                    print("Same name")
                                    x["Profile name :"] = profile
                                    if old_sd==new_SD and old_ed>new_SD and new_ED>old_ed:
                                        flag=1
                                        print("Same Name :First Case")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd>new_SD and old_ed>new_SD and old_ed<new_ED:
                                        print("Same Name :1.1 Case")
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd==new_SD and new_SD<old_ed and new_ED<old_ed:
                                        flag=1
                                        print("Same Name :second Case")
                                        x["End Date:"] = old_ed.strftime("%d-%m-%Y")
                                    elif old_sd<new_SD and new_SD< old_ed and new_ED<old_ed:
                                        flag = 1
                                        print("Same Name :2.1 Case")
                                        x["Start Date:"] = old_sd.strftime("%d-%m-%Y")
                                        x["End Date:"] = old_ed.strftime("%d-%m-%Y")
                                    elif old_ed==new_ED and old_ed>new_SD and old_sd>new_SD:
                                        print("Same Name :Third Case")
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                    elif old_ed==new_ED and new_ED>old_sd and new_SD>old_sd:
                                        flag = 1
                                        print("Same Name :Fourth Case")
                                        x["Start Date:"] = old_sd.strftime("%d-%m-%Y")
                                    elif old_sd<new_SD and old_ed>=new_SD and new_ED>old_ed:
                                        flag = 1
                                        print("Same Name :Fifth Case ")
                                        x["Start Date:"] = old_sd.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd==new_SD and old_ed==new_ED:
                                        print("Same Name :Sixth Case ")
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd>new_SD and old_sd<=new_ED and old_ed>new_ED:
                                        flag = 1
                                        print("Same Name :Seventh Case ")
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = old_ed.strftime("%d-%m-%Y")
                                else:
                                    if old_sd<new_SD and old_ed>=new_SD and old_ed<new_ED:
                                        print("first case ")
                                        x["End Date:"] = (new_SD - timedelta(days=1)).strftime("%d-%m-%Y")
                                    elif old_sd>new_SD  and  old_sd<=new_ED and new_ED<old_ed :
                                        print("Second case")
                                        x["Start Date:"]=(new_ED + timedelta(days=1)).strftime("%d-%m-%Y")
                                    elif old_ed==new_ED and old_ed>new_SD and old_sd<new_SD:
                                        print("Third case:")
                                        x["End Date:"] = (new_SD - timedelta(days=1)).strftime("%d-%m-%Y")
                                    elif old_sd==new_SD and old_ed>new_SD and old_ed>new_ED:
                                        print("fourth case")
                                        x["Start Date:"] = (new_ED + timedelta(days=1)).strftime("%d-%m-%Y")
                                    elif old_sd==new_SD and old_ed>new_SD and old_ed<new_ED:
                                        print("Fifth Case")
                                        x["Profile name :"]=profile
                                        x["Start Date:"] =new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] =new_ED.strftime("%d-%m-%Y")
                                    elif old_ed==new_ED and old_sd>new_SD and old_sd<new_ED:
                                        print("Sixth case")
                                        x["Profile name :"] = profile
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd ==new_SD and old_ed==new_ED:
                                        print("Seventh Case:")
                                        x["Profile name :"] = profile
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd>new_SD and old_sd<new_ED and old_ed<new_ED:
                                        print("Ninth case:")
                                        x["Profile name :"] = profile
                                        x["Start Date:"] = new_SD.strftime("%d-%m-%Y")
                                        x["End Date:"] = new_ED.strftime("%d-%m-%Y")
                                    elif old_sd<new_SD and new_ED>old_sd and old_ed>new_ED:
                                        print("Eighth Case:")
                                        x["End Date:"] = (new_SD - timedelta(days=1)).strftime("%d-%m-%Y")
                                        dis = new_ED + timedelta(days=1)
                                        dic.update({"Profile name :": x["Profile name :"]})
                                        dic.update({"Start Date:": dis.strftime("%d-%m-%Y")})
                                        dic.update({"End Date:": old_ed.strftime("%d-%m-%Y")})
                                        inside_data.append(dic)
                            if flag==0:
                                data.update({inputdata[0]: profile})
                                data.update({inputdata[1]: str_sd})
                                data.update({inputdata[2]: str_ed})
                                inside_data.append(data)
                                print("inside data", inside_data)
                                dictdata.update({p: sorted(inside_data, key= lambda x: datetime.strptime(x["Start Date:"],"%d-%m-%Y"))})
                                print("at last data append in if condition")
                                load_data.update(dictdata)
                        else:
                            print("new user added")
                            data.update({inputdata[0]: profile})
                            data.update({inputdata[1]: str_sd})
                            data.update({inputdata[2]: str_ed})
                            inside_data.append(data)
                            print("inside data", inside_data)
                            dictdata.update({p: sorted(inside_data, key=itemgetter("Start Date:"))})
                            print("at last data append in if condition")
                            load_data.update(dictdata)
                except Exception as e:
                    print(e,"sorry ....Exception Occur ")
                    print("load data",load_data)
    dictionary = {}
    for key, value in load_data.items():
        for x in value:
            my_final_json_data = [i for n, i in enumerate(value) if i not in value[n + 1:]]
        dictionary.update({key: my_final_json_data})
    print("Final dictionary:",dictionary)
    with open("dictionary_list.json", "w") as f:
        dump(dictionary, f, indent=2)


