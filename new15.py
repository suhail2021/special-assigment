start_num = int(20)  
end_num = int(50) 
cnt = start_num 
while cnt <= end_num:  
    if cnt % 7 == 0 and cnt % 5 == 0: 
        print(cnt, " is divisible by 7 and 5.")  
    cnt += 1