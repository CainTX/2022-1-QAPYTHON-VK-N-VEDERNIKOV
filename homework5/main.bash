echo "Общее количество запросов:" > bash_test.txt
awk '{print $0}' access.log | wc -l >> bash_test.txt
echo -e "\n" >> bash_test.txt
echo "Общее количество запросов по типу:" >> bash_test.txt
awk -F\" '{print $2}' access.log | awk '{print $1}'| sort | uniq -c >> bash_test.txt
echo -e "\n" >> bash_test.txt
echo "Топ 10 самых частых запросов:" >> bash_test.txt
awk -F\" '{print $2}' access.log | awk '{print $2}'| sort | uniq -c | sort -n | tail -10 >> bash_test.txt
echo -e "\n" >> bash_test.txt
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской ошибкой:" >> bash_test.txt
awk  '{print $0}' access.log | awk '{if($9>399 && $9<500) print $1 " " $7 " " $9 " " $10}' | sort -n -k4 | tail -5 >> bash_test.txt
echo -e "\n" >> bash_test.txt
echo "Топ 5 пользователей по количеству запросов, которые заверщились серверной ошибкой:" >> bash_test.txt
awk  '{print $0}' access.log | awk '{if($9>499) print $1}' | uniq -c | sort -n | tail -5 >> bash_test.txt
