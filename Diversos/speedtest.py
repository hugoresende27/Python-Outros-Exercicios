# from speedtest import Speedtest

# st = Speedtest()

# print("DOWNLOAD::: " , st.dowload())
# print("UPLOAD::: " , st.upload())
#######################################################################


# import speedtest
# print(dir(speedtest))
#######################################################################


# import speedtest
# s = speedtest.Speedtest()
# s.get_best_server()
# s.download()
# s.upload()
# res = s.results.dict()
# print(res["download"], res["upload"], res["ping"])
#######################################################################


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
  
    print(st.download())  
  
elif option == 2: 
  
    print(st.upload())  
  
elif option == 3:  
  
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print(st.results.ping)  
  
else:
  
    print("Please enter the correct choice !") 