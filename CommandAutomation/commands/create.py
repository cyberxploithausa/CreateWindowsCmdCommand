import sys
import os
import time
#from venv import create
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cred  # my credentials
from webdriver_manager.chrome import ChromeDriverManager


os.system("cls" if os.name == 'nt' else 'clear')


def main(**kwargs):
    '''
    Describe what this command does
    Args:
        Your Args description

    Usage:
        Your Usage description
    :return:
    '''
    dir_name = kwargs.get('dir_name')
    sub_dir = kwargs.get('sub_dir')

    print("""

     ######  ##    ## ########  ######## ########  ##     ## ########  ##        #######  #### ######## 
    ##    ##  ##  ##  ##     ## ##       ##     ##  ##   ##  ##     ## ##       ##     ##  ##     ##    
    ##         ####   ##     ## ##       ##     ##   ## ##   ##     ## ##       ##     ##  ##     ##    
    ##          ##    ########  ######   ########     ###    ########  ##       ##     ##  ##     ##    
    ##          ##    ##     ## ##       ##   ##     ## ##   ##        ##       ##     ##  ##     ##    
    ##    ##    ##    ##     ## ##       ##    ##   ##   ##  ##        ##       ##     ##  ##     ##    
     ######     ##    ########  ######## ##     ## ##     ## ##        ########  #######  ####    ##


        Hello! Thank you for using the cyberxploit's command tool to create your project.
        please use to following as a guide:
        usage:
            create projectFolder projectSubFolder
        example:
            create minesweeper functions
        Note that we want to create the main project with some base python file (run.py) and a README
        which will contains the sub-projectfolder and in it lies some funtions created to maintain the 
        full functionality of the projects. 
         
            """)

    # To dos
    # create the base projects folder name
    # use nul > filename.txt
    # create 2 files in the base projects folder [1. the run.py file and 2. the README.md file]
    # create a function folder in the base projects folder
    # create a functions.py file in the function folder.

    time.sleep(0.5)
    print("📁 Checking if there is a directory of this name in the path...✔️")
    time.sleep(1)
    try:
        if not os.path.exists(dir_name):  # type: ignore
            print("📁 Creating the directory you specify...✔️")
            os.makedirs(f"{dir_name}/{sub_dir}")
        else:
            print(f"[-] Folder {dir_name} exists")
            print("[-] Please change the name of the directory.")
            sys.exit(1)
        files = ["run.py", "README.md"]
        for file in files:
            with open(os.path.join(dir_name, str(file)), 'a') as temp_file:  # type: ignore
                print("[+] Creating the base file and markdown file...✔️")
                #temp_file.write(file) Not needed because it putting the text into the created files
        time.sleep(1)
       

        # Moving into the created project folder to open visual studio code.
        print(f"[*] Changing to the project folder {dir_name} 📁")
        os.chdir(dir_name)  # type: ignore
        time.sleep(1)

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://github.com/login")

            # can say time.sleep(5) but implicitly_wait does the job without completing the full time
            # if the browser load faster before the specified wait time.
            driver.implicitly_wait(10)

            username = driver.find_element_by_xpath("//*[@id='login_field']")
            # replace cred.git_user with your github username
            username.send_keys(cred.git_user)

            password = driver.find_element_by_xpath("//*[@id='password']")
            # replace cred.git_pass with your github password
            password.send_keys(cred.git_pass)

            sign_in = driver.find_element_by_name("commit")
            sign_in.click()

            time.sleep(2)
            driver.implicitly_wait(30)
            New_repo = driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/header/div[6]/details/summary")
            # "/html/body/div[1]/header/div[6]/details/summary/span")
            New_repo.click()

            driver.implicitly_wait(5)
            # for _ in range(5):

            Click_repo = driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/header/div[6]/details/details-menu/a[1]")
                #"/html/body/div[1]/header/div[6]/details/details-menu/a[1]")
            Click_repo.click()

            time.sleep(3)
            repo = driver.find_element_by_xpath("//*[@id='repository_name']")
            repo.send_keys(dir_name)  # name of repository

            mid = driver.find_element_by_tag_name('body')
            time.sleep(1)
            mid.send_keys(Keys.END)
            driver.implicitly_wait(10)

            create_repo = driver.find_element_by_xpath(
                '//*[@id="new_repository"]/div[5]/button')
            #create_repo = driver.find_element_by_class_name("btn-primary btn")
            # create_repo = driver.find_element_by_css_selector('#new_repository > div.js-with-permission-fields > button')
            create_repo.click()
            time.sleep(5)

            # clearing the screen for the other git commands
            # Right i push every single local file and folder to the new repository.
            print("clearing Console...")
            os.system("cls" if os.name == 'nt' else "clear")
            time.sleep(2)
            print("Initializing empty git.")
            os.system("git init")
            time.sleep(2)
            print("Adding *Everything to repo")
            os.system("git add .")
            time.sleep(2)
            print("Commiting first")
            os.system('git commit -m "first commit"')
            time.sleep(4)
            print("Branch name: main")
            os.system("git branch -M main")
            time.sleep(5)
            print("Remote adding main branch")
            # file deepcode ignore CommandInjection: <please specify a reason of ignoring this>
            os.system(
                f"git remote add origin https://github.com/cyberxploit/{dir_name}.git")
            time.sleep(2)
            print("Pushing *Everything to repo")
            time.sleep(2)
            os.system("git push -u origin main")
            time.sleep(2)
            print(f"    Moved to {dir_name} 📁 successfully.")
            time.sleep(2)
            print("[+] Successfully  created a repository...")
            # Opening VS Code in the base Created Project folder.
            time.sleep(3)
            os.system('code .')
            time.sleep(2)
        except Exception:
            print("Something is wrong")
            # print(e)

    except TypeError:
        time.sleep(1)
        print("You have to specify the project name and the sub-project folder.")
        time.sleep(0.8)
        print(
            """example:
                create minesweeper functions
            """
        )


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        'dir_name',
        'sub_dir'
    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)
