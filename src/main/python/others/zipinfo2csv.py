import zipfile
import os
import datetime, time
import csv

user_generate_path = "/data/cer-data/user_generate_file"
files = os.listdir(user_generate_path)
csv_content = []
column_title = ["org_code", "template_type", "template_name", "file_name", "template_person_num",
                "template_enterprise_num", "expect_num", "actual_num", "rx_insertTime", "rx_updateTime"]
total_2_m_zip = 0
for type_file in files:
    print("cur_temp_typ:" + type_file)
    if os.path.isdir(type_file):
        type_path = user_generate_path + "/" + type_file
        user_templ_count_map = {}
        for user_file in os.listdir(type_path):
            if user_file == "optd":
                continue
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
                            row_content = [""] * 10
                            print("cur_zip:" + zip)
                            zip_path = templ_path + "/" + zip
                            file_time = time.localtime(os.stat(zip_path).st_ctime)
                            y = time.strftime('%Y', file_time)
                            m = time.strftime('%m', file_time)
                            d = time.strftime('%d', file_time)
                            H = time.strftime('%H', file_time)
                            M = time.strftime('%M', file_time)
                            S = time.strftime('%S', file_time)
                            file_d_time = datetime.datetime(int(y), int(m), int(d), int(H), int(M), int(S))
                            # t = (file_d_time - datetime.datetime(2018, 1, 31))
                            # if t > 0:
                            #     total_2_m_zip += 1
                            #     continue

                            z_file = zipfile.ZipFile(zip_path)
                            count = 0
                            for f in z_file.filelist:
                                count += 1

                            # org_name
                            row_content[0] = user_file
                            # template_name
                            row_content[2] = templ_name
                            # file_name
                            row_content[3] = zip
                            # template_person_num
                            # tempalte_enterprise_num
                            person_num = enter_num = 0
                            tpl_type = 1
                            if type_file == "PERSONAL":
                                person_num = count
                                tpl_type = 1
                            elif type_file == "ORGANIZATION":
                                enter_num = count
                                tpl_type = 2
                            else:
                                person_num = enter_num = count
                                tpl_type = 3
                            # template_type
                            row_content[1] = tpl_type
                            row_content[4] = person_num
                            row_content[5] = enter_num
                            # expext_num
                            # actual_num
                            row_content[6] = row_content[7] = count
                            csv_content.append(row_content)
                            # time
                            row_content[8] = row_content[9] = str(file_d_time)
                        temp_name_count_map[templ_name] = templ_count

csv_path = user_generate_path + "/" + "history.csv"
if os.path.exists(csv_path):
    os.remove(csv_path)
f = open(csv_path, "wb+")
# write bom to resolve unreadable chinese problem
f.write("\xEF\xBB\xBF")
writer = csv.writer(f)
# write csv title
writer.writerow(column_title)
# write csv content
for line in csv_content:
    writer.writerow(line)
