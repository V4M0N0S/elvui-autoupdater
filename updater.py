import os
import requests
import zipfile
import shutil

github_zip_url = "https://github.com/tukui-org/ElvUI/archive/refs/heads/main.zip"

# ------------------------------------------------------------------------------

# Change your target folder here
target_dir = "C:/ProgramFiles(x86)/WorldofWarcraft/_retail_/Interface/AddOns"

# ------------------------------------------------------------------------------

response = requests.get(github_zip_url)

if response.status_code == 200:
    with open("elvui.zip", "wb") as zip_file:
        zip_file.write(response.content)

    with zipfile.ZipFile("elvui.zip", "r") as zip_ref:

        for folder in ["ElvUI", "ElvUI_Libraries", "ElvUI_Options"]:
            folder_path = os.path.join(target_dir, folder)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)

        zip_ref.extractall("temp_folder")

        for folder in ["ElvUI", "ElvUI_Libraries", "ElvUI_Options"]:
            source_path = os.path.join("temp_folder", f"ElvUI-main/{folder}")
            dest_path = os.path.join(target_dir, folder)
            shutil.copytree(source_path, dest_path)

        os.remove("elvui.zip")
        shutil.rmtree("temp_folder")

else:
    print("Error")

exit()
