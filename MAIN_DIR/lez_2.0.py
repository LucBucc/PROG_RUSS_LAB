#[15/11/22]_________________________ [15 NOV 2022]


#___Printiamo due variabili insieme usando .format
my_var1 = "banane"           
#la stringa va tra virgolette o non capisce
my_var2 = 416.17999999999999
print ("Valore 1: {}, Valore 2: {}".format(my_var1, my_var2))
#le virgolette del print finiscono prima del punto, poi va inserito un comando (una funzione?) che ha degli argomenti  (le variabili precedentemente dichiarate my_var).
##########################################
print (my_var1[0:4])
#stampo i caratteri 0,1,2,3 di my_var1
#( 0=b - 1=a - 2=n - 3=a)
##########################################
print (my_var1[2:-1])
#dal carattere numero 3 al penultimo
#ricordati che i caratteri li conta da 0, ecco perchè 3.
##########################################
print (my_var1[4:2], "       <---non fa")
#.............non fa un c@zzo
#########################################
a = 0
if ("a" in my_var1) :
    a = 1
print(a)






