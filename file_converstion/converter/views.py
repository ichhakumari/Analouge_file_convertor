
from django.conf import settings
import os
from django.shortcuts import render
from django.http import JsonResponse
from subprocess import run
from .forms import FileUploadForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def conversion(request):
    return render(request, 'conversion.html')


def split(request):
    return render(request, 'split.html')



UPLOAD_DIR = "uploads/"
OUTPUT_DIR = "converted/"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

#======================================================================================================================
#smi to sdf
def convert_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        output_filename = uploaded_file.name.replace(".smi", ".sdf")
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"Input file saved at: {input_path}")  
        print(f"Output file path: {output_path}")  

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Convert
        command = ["obabel", "-ismi", input_path, "-osdf", "--gen3D",  "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")  
        print(f"Open Babel Error: {result.stderr}")  

        

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"  
            print(f"Conversion Successful: {file_url}") 
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})

#======================================================================================================================
def sdf_smi(request):
    return render(request, 'sdftosmi.html')

def sdf_to_smi(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".sdf", ".smi")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-isdf", input_path, "-osmi", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
            messages.success(request, "Conversion Completed Successfully!") 
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            messages.error(request, "Conversion Failed!")
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})

#======================================================================================================================

def smi_pdb(request):
    return render(request, 'smitopdb.html')

def smi_to_pdb(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".smi", ".pdb")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-ismi", input_path, "-opdb","--gen3D", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
            messages.success(request, "Conversion Completed Successfully!") 
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            messages.error(request, "Conversion Failed!")
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})


#======================================================================================================================

def pdb_smi(request):
    return render(request, 'pdbtosmi.html')

def pdb_to_smi(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".pdb", ".smi")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-ipdb", input_path, "-osmi", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
            messages.success(request, "Conversion Completed Successfully!") 
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            messages.error(request, "Conversion Failed!")
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})



#======================================================================================================================



def sdf_pdb(request):
    return render(request, 'sdftopdb.html')

# def sdf_to_pdb(request):
#     if request.method == 'POST' and request.FILES.get('file'): 
#         uploaded_file = request.FILES['file']
#         input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
#         output_filename = uploaded_file.name.replace(".sdf",".pdb")  
#         output_path = os.path.join(OUTPUT_DIR, output_filename)  

#         print(f"Input file saved at: {input_path}")
#         print(f"Output file path: {output_path}")

#         # Save uploaded file
#         with open(input_path, 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)

#         # Open Babel command
#         command = ["obabel", "-isdf", input_path, "-opdb", "-O", output_path]
#         result = run(command, capture_output=True, text=True)

#         print(f"Open Babel Output: {result.stdout}")
#         print(f"Open Babel Error: {result.stderr}")

#         if os.path.exists(output_path):
#             file_url = f"{settings.MEDIA_URL}{output_filename}"
#             print(f"Conversion Successful: {file_url}")
#             messages.success(request, "Conversion Completed Successfully!") 
#             return JsonResponse({"success": True, "file_url": file_url})

#         else:
#             print(f"Conversion Failed: {result.stderr}")
#             messages.error(request, "Conversion Failed!")
#             return JsonResponse({"success": False, "error": result.stderr})

#     return JsonResponse({"success": False, "error": "Invalid request"})


from django.contrib import messages 

def sdf_to_pdb(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".sdf", ".pdb")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-isdf", input_path, "-opdb", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            success_message = "Conversion Completed Successfully!"
            messages.success(request, success_message)
            return JsonResponse({"success": True, "file_url": file_url, "message": success_message})

        else:
            error_message = "Conversion Failed!"
            messages.error(request, error_message)
            return JsonResponse({"success": False, "error": result.stderr, "message": error_message})

    return JsonResponse({"success": False, "error": "Invalid request", "message": "Invalid Request"})


#======================================================================================================================
#pdb_to_sdf



def pdb_sdf(request):
    return render(request, 'pdbtosdf.html')

def pdb_to_sdf(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".pdb", ".sdf")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-ipdb", input_path, "-osdf", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
          
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
         
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})



#======================================================================================================================
#smi_to_mol2

def smi_mol2(request):
    return render(request, 'smitomol2.html')

def smi_to_mol2(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".smi", ".mol2")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-ismi", input_path, "-omol2","--gen3D", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
            
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
           
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})




#======================================================================================================================

#mol2_to_smi

def mol2_smi(request):
    return render(request, 'mol2tosmi.html')

def mol2_to_smi(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".mol2", ".smi")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-imol2", input_path, "-osmi", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
            
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
           
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})




#======================================================================================================================
#sdf to mol2 


def sdf_mol2(request):
    return render(request, 'sdftomol2.html')

def sdf_to_mol2(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".sdf", ".mol2")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-isdf", input_path, "-omol2", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
          
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})


#======================================================================================================================
#mol2 to sdf


def mol2_sdf(request):
    return render(request, 'mol2tosdf.html')

def mol2_to_sdf(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".mol2" ,".sdf")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-imol2", input_path, "-osdf", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
          
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})



#======================================================================================================================
#pdb to ,mol2

def pdb_mol2(request):
    return render(request, 'pdbtomol2.html')

def pdb_to_mol2(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".pdb", ".mol2")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-ipdb", input_path, "-omol2", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
          
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})


#======================================================================================================================
# mol2_to_pdb

def mol2_pdb(request):
    return render(request, 'mol2topdb.html')

def mol2_to_pdb(request):
    if request.method == 'POST' and request.FILES.get('file'): 
        uploaded_file = request.FILES['file']
        input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)  
        output_filename = uploaded_file.name.replace(".mol2", ".pdb")  
        output_path = os.path.join(OUTPUT_DIR, output_filename)  

        print(f"Input file saved at: {input_path}")
        print(f"Output file path: {output_path}")

        # Save uploaded file
        with open(input_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Open Babel command
        command = ["obabel", "-imol2", input_path, "-opdb", "-O", output_path]
        result = run(command, capture_output=True, text=True)

        print(f"Open Babel Output: {result.stdout}")
        print(f"Open Babel Error: {result.stderr}")

        if os.path.exists(output_path):
            file_url = f"{settings.MEDIA_URL}{output_filename}"
            print(f"Conversion Successful: {file_url}")
          
            return JsonResponse({"success": True, "file_url": file_url})

        else:
            print(f"Conversion Failed: {result.stderr}")
            
            return JsonResponse({"success": False, "error": result.stderr})

    return JsonResponse({"success": False, "error": "Invalid request"})


#======================================================End================================================================
