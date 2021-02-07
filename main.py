from spider import Spider

if __name__=='__main__':  
    s = Spider()
    s.sp()
    print(len(s.data))
    ret = []
    for d in s.data:
        type = d['type']
        if type != "0":
            data = {}
            data['user_nicename'] = d['user_nicename']
            data['title'] = d['title']
            # data['city'] = d['city']
            data['pull'] = d['pull']
            print(d)
            ret.append(data)
            print(data,"\n\n")
    # print(ret)
        
