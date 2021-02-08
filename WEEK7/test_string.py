file = open('WEEK7/shampoo_sales.csv','r')

for i,line in enumerate(file):
    count = 0;
    if(i<=10):
        print("This line {}".format(i))
        print("Line: {}".format(line))
        for el in line:
            if(el=='\n' or el==' ' or el=='\0'):
                print("End of line\n")  
            else:
                print("Element:{}".format(el))
         
    else:
        break;

file.close()
