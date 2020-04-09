import sys

input,output=sys.argv[1],sys.argv[2]

def bubble_sort(list1):

    n = len(list1)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    return list1


def frekans_with_dict(list2):

    frekans_dict = {}

    for item in list2:
        item=int(item)
        if item in frekans_dict :
            frekans_dict[item] = frekans_dict[item] + 1
        else:
            frekans_dict[item] = 1

    print(frekans_dict)

    return frekans_dict

def mod_with_dict(my_hist_d):
    frekans_max = -1
    mod = -1

    for key in my_hist_d.keys():

        if my_hist_d[key] > frekans_max:
            frekans_max = my_hist_d[key]
            mod = key

    return mod,frekans_max

def medyan_bulma(dizi1):

    dizi1= bubble_sort(dizi1)

    if len(dizi1)%2==1:

        orta = int(len(dizi1)/2)+1
        return dizi1[orta-1]

    else:
        median1,median2=dizi1[int(len(dizi1)/2)],dizi1[int(len(dizi1)/2)-1]
        return (median1+median2)/2



def Liste_ort(liste1):
    toplam = 0
    s=0
    for item in liste1:
        toplam += int(item)
        s += 1

    return int(toplam/s)



with open(input+"input_hw_2.csv", "r") as dosya:
    data = []
    data1 = dosya.read()
    data_line = data1.split(';')
    data.append(data_line)

    date = []
    ayir = []
    for i in range(3, len(data_line), 3):

        ayir.append(data_line[i].split("-"))

    aylar = []
    for i in range(len(ayir)):
        aylar.append(int(ayir[i][1]))

bubble_sort(aylar)
a = frekans_with_dict(aylar)
newlist = [a[i] for i in a]



with open(output+"180401047_hw_2_output.txt", "w") as dosya:

    dosya.write("Medyan :"+ "" + str(medyan_bulma(newlist))+"\n")
    dosya.write("Ortalama:" + ""+ str(Liste_ort(newlist)))
