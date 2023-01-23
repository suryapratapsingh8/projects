

# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:

1) Download Speed

2) Upload Speed

3) Ping

Your Choice: '''))


if option == 1:

	print(str(st.download()//1000000)+'MBPS')

elif option == 2:

	print(str(st.upload()//1000000)+ 'MBPS')

elif option == 3:

	servernames =[]

	st.get_servers(servernames)

	print(str(st.results.ping)+'NMS')

else:

	print("Please enter the correct choice !")

