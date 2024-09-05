Hour = int(input("Enter Start Hour:"))                 
Minute = int(input("Enter Start Minutes:"))
Duration_Hour = int(input("Enter Duration Hour:"))
Duration_Minute = int(input("Enter Duration Minutes:"))

Total_Time_In_Minutes = (Hour + Duration_Hour) * 60 + (Minute + Duration_Minute)

End_Hour = Total_Time_In_Minutes // 60
End_Minute = Total_Time_In_Minutes % 60

print("The meeting will end by ", End_Hour, ":", End_Minute)          
