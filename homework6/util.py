import copy
import os


def assignment():
    global indicator
    text = ''
    while current_line[indicator] != ' ':
        text += current_line[indicator]
        indicator += 1
    indicator += 1
    return text


def text_skip(skip):
    global indicator
    while current_line[indicator] != '"':
        indicator += 1
    indicator += skip


def size_check(size):
    int_check = True
    for i in range(len(size)):
        if (ord(size[i]) < ord('0')) or (ord(size[i]) > ord('9')):
            int_check = False
    return int_check


def data_frequent_requests(url):
    global list_test3
    place = 10
    match = 10
    for i in range(9, -1, -1):
        if list_test3[i][2] < url_dict[url]:
            place = i
        if list_test3[i][1] == url:
            match = i
    if place != 10:
        if match != 10:
            list_test3[match][1] = list_test3[place][1]
            list_test3[match][2] = list_test3[place][2]
        list_test3[place][1] = url
        list_test3[place][2] = url_dict[url]


def status_code_check(status_code):
    if 400 <= status_code < 500:
        current_status_code = '4XX'
    elif 500 <= status_code < 600:
        current_status_code = '5XX'
    else:
        current_status_code = 'WRONG'
    return current_status_code


def data_requests_client_error(size, url, status_code, ip):
    global list_test4
    for i in range(5):
        if size > list_test4[i][3]:
            for j in range(4, i, -1):
                for r in range(1, 5):
                    list_test4[j][r] = list_test4[j - 1][r]
            list_test4[i][1] = url
            list_test4[i][2] = status_code
            list_test4[i][3] = size
            list_test4[i][4] = ip
            break


def data_requests_server_error(ip):
    global list_test5
    place = 5
    match = 5
    for i in range(4, -1, -1):
        if list_test5[i][2] < ip_dict[ip]:
            place = i
        if list_test5[i][1] == ip:
            match = i
    if place != 5:
        if match != 5:
            list_test5[match][1] = list_test5[place][1]
            list_test5[match][2] = list_test5[place][2]
        list_test5[place][1] = ip
        list_test5[place][2] = ip_dict[ip]


def result_total_requests():
    request_count_copy = copy.deepcopy(request_count)
    return request_count_copy


def result_total_requests_type():
    list_test2_copy = copy.deepcopy(list_test2)
    return list_test2_copy


def result_top_frequent_requests():
    list_test3_copy = copy.deepcopy(list_test3)
    return list_test3_copy


def result_requests_client_error():
    list_test4_copy = copy.deepcopy(list_test4)
    return list_test4_copy


def result_requests_server_error():
    list_test5_copy = copy.deepcopy(list_test5)
    return list_test5_copy


base_dir = ("/home/runner/work/2022-1-QAPYTHON-VK-N-VEDERNIKOV/2022-1-QAPYTHON-VK-N-VEDERNIKOV/homework6/access.log")
logfile = open(base_dir)
request_count = [[0] for i in range(1)]
method_dict = dict.fromkeys(['GET', 'PUT', 'HEAD', 'POST'], 0)
ip_dict = dict()
url_dict = dict()
list_test3 = [[0] * 3 for i in range(10)]
list_test4 = [[0] * 5 for i in range(5)]
list_test5 = [[0] * 3 for i in range(5)]
for i in range(5):
    list_test3[i][0] = i + 1
    list_test4[i][0] = i + 1
    list_test5[i][0] = i + 1
for i in range(5, 10):
    list_test3[i][0] = i + 1
for line in logfile:
    current_line = line
    indicator = 0
    request_count[0][0] += 1
    ip = assignment()
    text_skip(1)
    method = assignment()
    url = assignment()
    text_skip(2)
    status_code = int(assignment())
    size = assignment()
    url_dict[url] = url_dict.get(url, 0) + 1
    ip_dict[ip] = ip_dict.get(ip, 0) + 1
    if method_dict.get(method) is not None:
        method_dict[method] += 1
    data_frequent_requests(url)
    status_param = status_code_check(status_code)
    if status_param == '5XX':
        data_requests_server_error(ip)
    elif status_param == '4XX':
        size_param = size_check(size)
        if size_param:
            data_requests_client_error(int(size), url, status_code, ip)
list_test2 = list(method_dict.items())
logfile.close()
