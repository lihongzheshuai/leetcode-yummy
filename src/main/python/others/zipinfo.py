import zipfile
import os
import datetime,time

user_generate_path = "/data/cer-data/user_generate_file"
files = os.listdir(user_generate_path)
template_type = {}
total_2_m_zip = 0
for type_file in files:
    print("cur_temp_typ:" + type_file)
    if os.path.isdir(type_file):
        type_path = user_generate_path + "/" + type_file
        user_templ_count_map = {}
        for user_file in os.listdir(type_path):
            print("cur_user:" + user_file)
            user_path = type_path + "/" + user_file
            if os.path.isdir(user_path):
                temp_name_count_map = {}
                for templ_name in os.listdir(user_path):
                    print("cur_temp_name:" + templ_name)
                    templ_path = user_path + "/" + templ_name
                    if os.path.isdir(templ_path):
                        templ_count = 0
                        for zip in os.listdir(templ_path):
                            print("cur_zip:" + zip)
                            zip_path = templ_path + "/" + zip
                            file_time = time.localtime(os.stat(zip_path).st_ctime)
                            y = time.strftime('%Y', file_time)
                            m = time.strftime('%m', file_time)
                            d = time.strftime('%d', file_time)
                            H = time.strftime('%H', file_time)
                            M = time.strftime('%M', file_time)
                            file_d_time = datetime.datetime(int(y), int(m), int(d), int(H), int(M))
                            t = (file_d_time - datetime.datetime(2018, 1, 31))
                            if t > 0:
                                total_2_m_zip += 1
                                continue
                            z_file = zipfile.ZipFile(zip_path)
                            count = 0
                            for f in z_file.filelist:
                                count += 1
                            # print(zip_path + "[" + str(count) +"]")
                            templ_count += count
                            #print(templ_count)
                        temp_name_count_map[templ_name] = templ_count
                print(str(temp_name_count_map))
                user_templ_count_map[user_file] = temp_name_count_map
        template_type[type_file] = user_templ_count_map

print("Feb zip: [" + str(total_2_m_zip) + "]")
for type, users in template_type.items():
    print("template_type:[" + str(type) +  "]")
    for user, templ in users.items():
        print("user: [" + str(user) + "]")
        for templ, count in templ.items():
            print("temp_name:[" + str(templ) + "], count: [" + str(count) + "]")
