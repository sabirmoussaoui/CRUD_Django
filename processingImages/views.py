from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from processingImages.ImageProcessing import ImageProcessing
from processingImages.Optimisation import Optimisation
opt = Optimisation()



def index(request):
    return render(request, 'processingImage/index.html')
# -*- coding: utf-8 -*-
def getPathImage(request):
    if request.method == 'POST':
       myfile = request.FILES['myfile']
       fs = FileSystemStorage()
       filename = fs.save(myfile.name, myfile)
       uploaded_file_url = fs.url(filename)
       print(uploaded_file_url)
       return render(request,'processingImage/figure.html')
# -*- coding: utf-8 -*-


#ProcessingImage
def getProcessingImage(request):
    myfile = request.FILES['myfile']
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    path_img = "processingImages/image/"+str(myfile)
    print(path_img)
    imgp = ImageProcessing(path_img)
    fig_image, image_2D = imgp.importer_img()
    fig_histogramme = imgp.copy_img_cree_hist(image_2D)
    fig_image_binaire,image_binaire = imgp.cree_image_binaire(image_2D)
    fig_enlever_artefacts,image_enlever_artefacts = imgp.enlever_artefacts(image_binaire)
    # Segmentation de l'image: label_image contient les différents labels et n_labels est le nombre de labels
    print("********************Segmentation de l'image")
    label_image, n_label = imgp.segmenter_image(image_enlever_artefacts)
    # Visualisation de l'image étiquetée
    print("********************Visualisation de l'image étiquetée")
    fig_image_etiquete =imgp.show_image_etiquete(label_image)
    # Mesure de la taille de chaque groupes de label_images (fait la somme des pixels)
    print("******************** Mesure de la taille de chaque groupes de label_images (fait la somme des pixels)")
    sizes = imgp.mesurer_taille(image_enlever_artefacts, label_image, n_label)
    # Visualisation des résultats
    fig_result=imgp.show_result(sizes, n_label)
    return render(request, 'processingImage/figure.html',
                  {'figure_image': fig_image,
                   'fig_histogramme': fig_histogramme,
                   'fig_image_binaire': fig_image_binaire,
                   'fig_enlever_artefacts': fig_enlever_artefacts,
                   'n_label': n_label,
                   'fig_image_etiquete': fig_image_etiquete,
                   'fig_result': fig_result})





# def getImage(request):
#     return render(request,'processingImage/figure.html',{'data':fig_image})
# def getHistImage(request):
#     return render(request,'processingImage/figure.html',{'data':fig_histogramme})
#Optimisation
def showNuage(request):
    return render(request,'processingImage/figure.html',{'data':opt.show_nuage()})

def getModel(request):
    params = opt.getParam()
    return render(request,'processingImage/figure.html',{'data':opt.showResult(params)})
#Importer file
