import sys
#f = open("./TensoRF_jiwon/measurement/lb_test10.txt", 'r')
file_name = sys.argv[1]
f = open(file_name)

lines = f.readlines()
#print(lines)


metrics = dict()


for l in lines:
    if "JW-" in l:
    #if l.find("[JW-")>=0:
        function_name = l.split()[0]
        #print(function_name)
        if function_name not in metrics:
            metrics[function_name]= []
        metrics[function_name].append(float(l.split(":")[1]))


print("<Total>")
for m in metrics:
    print("{} {}".format(m, sum(metrics[m])))

print("<Average>")
for m in metrics:
    print("{} {}".format(m, sum(metrics[m])/len(metrics[m])))
    #print(m)
    #print(metrics[m])
    #print(sum(metrics[m])/len(metrics[m]))
    #print(len(metrics[m]))

