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


def test3(url):
    global list_test3
    place = 10
    match = 10
    for i in range(9, -1, -1):
        if list_test3[1][i] < url_dict[url]:
            place = i
        if list_test3[0][i] == url:
            match = i
    if place != 10:
        if match != 10:
            list_test3[0][match] = list_test3[0][place]
            list_test3[1][match] = list_test3[1][place]
        list_test3[0][place] = url
        list_test3[1][place] = url_dict[url]


def status_code_check(status_code):
    if 400 <= status_code < 500:
        current_status_code = '4XX'
    elif 500 <= status_code < 600:
        current_status_code = '5XX'
    else:
        current_status_code = 'WRONG'
    return current_status_code


def test4(size, url, status_code, ip):
    global list_test4
    for i in range(5):
        if size > list_test4[2][i]:
            for j in range(4, i, -1):
                for r in range(4):
                    list_test4[r][j] = list_test4[r][j - 1]
            list_test4[0][i] = url
            list_test4[1][i] = status_code
            list_test4[2][i] = size
            list_test4[3][i] = ip
            break


def test5(ip):
    global list_test5
    place = 5
    match = 5
    for i in range(4, -1, -1):
        if list_test5[1][i] < ip_dict[ip]:
            place = i
        if list_test5[0][i] == ip:
            match = i
    if place != 5:
        if match != 5:
            list_test5[0][match] = list_test5[0][place]
            list_test5[1][match] = list_test5[1][place]
        list_test5[0][place] = ip
        list_test5[1][place] = ip_dict[ip]


logfile = open('access.log')
python_test = open('python_test.txt', 'wt')
request_count = 0
method_dict = dict.fromkeys(['GET', 'PUT', 'HEAD', 'POST', 'POP'], 0)
ip_dict = dict()
url_dict = dict()
list_test3 = [[0] * 10 for i in range(2)]
list_test4 = [[0] * 5 for i in range(4)]
list_test5 = [[0] * 5 for i in range(2)]
for line in logfile:
    current_line = line
    indicator = 0
    request_count += 1
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
    test3(url)
    status_param = status_code_check(status_code)
    if status_param == '5XX':
        test5(ip)
    elif status_param == '4XX':
        size_param = size_check(size)
        if size_param == True:
            test4(int(size), url, status_code, ip)
python_test.write('Общее количество запросов: \n' + str(request_count))
python_test.write('\n\nОбщее количество запросов по типу: \n')
python_test.write('GET: ' + str(method_dict['GET']) + ', PUT: ' + str(method_dict['PUT']) + ', HEAD: ' + str(
    method_dict['HEAD']) + ', POST: ' + str(method_dict['POST']))
python_test.write('\n\nТоп 10 самых частых запросов: \n')
for i in range(10):
    python_test.write(str(i + 1) + ')' + ' ' + list_test3[0][i] + ' ' + str(list_test3[1][i]) + '\n')
python_test.write('\nТоп 5 самых больших по размеру запросов, которые завершились клиентской ошибкой (4XX)')
for i in range(5):
    python_test.write('\n' + str(i + 1) + ')' + ' ' + list_test4[0][i] + ' ' + str(list_test4[1][i]) + ' ' + str(
        list_test4[2][i]) + ' ' + list_test4[3][i])
python_test.write('\n\nТоп 5 пользователей по количеству запросов, которые завершились серверной ошибкой (5XX)')
for i in range(5):
    python_test.write('\n' + str(i + 1) + ')' + ' ' + list_test5[0][i] + ' ' + str(list_test5[1][i]))
logfile.close()
python_test.close()
