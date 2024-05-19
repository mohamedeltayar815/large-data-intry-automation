from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


import time
from datalists import mylist19


def perform_registration(url, username, password):
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Open the provided URL
    driver.get(url)

    try:
        # Click on the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cntphmaster_DataOrgStructureNode1_btnSearch"))
        )
        search_button.click()

        codebl_input = driver.find_element(By.ID, "cntphmaster_DataOrgStructureNode1_txtNodeCode")
        codebl_input.send_keys("6241")

        codebl_button = driver.find_element(By.ID, "cntphmaster_DataOrgStructureNode1_btnSearchNode")
        codebl_button.click()

        

        # Click on the specified tree nodes
        tree_nodes = ["cntphmaster_DataOrgStructureNode1_TreeView1n0",
                      "cntphmaster_DataOrgStructureNode1_TreeView1n1",
                      "cntphmaster_DataOrgStructureNode1_TreeView1n2",
                      "cntphmaster_DataOrgStructureNode1_TreeView1n3",
                      "cntphmaster_DataOrgStructureNode1_TreeView1t3",
                      ]
        for node_id in tree_nodes:
            tree_node = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, node_id))
            )
            tree_node.click()

        # Input username
        username_input = driver.find_element(By.ID, "cntphmaster_txtUsername")
        username_input.send_keys(username)

        # Input password
        password_input = driver.find_element(By.ID, "cntphmaster_txtPassword")
        password_input.send_keys(password)

        # Click on the login button
        login_button = driver.find_element(By.ID, "cntphmaster_btnLogin")
        login_button.click()
        time.sleep(1)

        #goto imploe data 
        impdata_button = driver.find_element(By.ID, "cntphmaster_btnEmployee")
        impdata_button.click()

        time.sleep(1)

        #cntphmaster_DataOrgStructureNode1_btnSearch
        cntphmaster_button = driver.find_element(By.ID, "cntphmaster_DataOrgStructureNode1_btnSearch")
        cntphmaster_button.click()
        time.sleep(1)

        #cntphmaster_DataOrgStructureNode1_TreeView1t0
        TreeView1t0_button = driver.find_element(By.ID, "cntphmaster_DataOrgStructureNode1_TreeView1t0")
        TreeView1t0_button.click()
        
        
        time.sleep(1)

        #cntphmaster_btnGo
        cntphmaster_btnGo_button = driver.find_element(By.ID, "cntphmaster_btnGo")
        cntphmaster_btnGo_button.click()

        time.sleep(1)

        #cntphmaster_btnAdd
        cntphmaster_btnAdd_button = driver.find_element(By.ID, "cntphmaster_btnAdd")
        cntphmaster_btnAdd_button.click()

        time.sleep(2)

        # main code do looping in datta and registeration 

        def data_operator():
            for item in mylist19:
                yield item

        def data_ork(operator=None):
            if operator is None:
                operator = data_operator()

            try:
                obj = next(operator)
            except StopIteration:
                print("All work done correctly!")
                return
# { 'f_name': 'فاطمه',  'sc_name': 'بهاء الدين',  'thr_name': 'ابراهيم',  'ls_name': 'حسن',  'nat_id': 29501172102946,  'st_date': '2017-06-01 ',  'phone_num':'01115669829',  'grad_year': 2016 },

            def fr_page():
                print(obj["f_name"])

                fn_input = driver.find_element(By.ID, "cntphmaster_txtNameFirst")
                fn_input.send_keys(obj["f_name"])

                time.sleep(1)

                scn_input = driver.find_element(By.ID, "cntphmaster_txtNameSecond")
                scn_input.send_keys(obj["sc_name"])

                time.sleep(1)

                thrn_input = driver.find_element(By.ID, "cntphmaster_txtNameThird")
                thrn_input.send_keys(obj["thr_name"])

                time.sleep(1)

                lasn_input = driver.find_element(By.ID, "cntphmaster_txtNameFourth")
                lasn_input.send_keys(obj["ls_name"])

                time.sleep(1)

                id_input = driver.find_element(By.ID, "cntphmaster_txtNationalId")
                id_input.send_keys(obj["nat_id"])

                time.sleep(1)

                dropdown_mar_input = Select(driver.find_element(By.ID, "cntphmaster_drpRefMaritalStatusId"))
                dropdown_mar_input.select_by_value("2")
                
                time.sleep(1)

                choselocal_button = driver.find_element(By.ID, "cntphmaster_DataLocNode1_btnSearch")
                choselocal_button.click()

                time.sleep(1)

                conf_choselocal_button = driver.find_element(By.ID, "cntphmaster_DataLocNode1_TreeView1t7")
                conf_choselocal_button.click()

                time.sleep(1)

                dropdown_work_input = Select(driver.find_element(By.ID, "cntphmaster_drpDOSNIDBR"))
                dropdown_work_input.select_by_value("4356")
                
                time.sleep(1)

                fr_submit_button = driver.find_element(By.ID, "cntphmaster_btnSave")
                fr_submit_button.click()

                time.sleep(3)

                fr_next_button = driver.find_element(By.ID, "cntphmaster_BtnNext")
                fr_next_button.click()

                time.sleep(3)





                #submit id = cntphmaster_btnSave
                #submit id = cntphmaster_BtnNext



            def sc_page():
                print(obj["sc_name"])

                dropdown_phone_input = Select(driver.find_element(By.ID, "cntphmaster_drpGsCodeContactMethodId"))
                dropdown_phone_input.select_by_value("2")
                
                time.sleep(1)

                phone_input = driver.find_element(By.ID, "cntphmaster_txtMethodValue")
                phone_input.send_keys(obj["phone_num"])

                time.sleep(1)

                sc_submit_button = driver.find_element(By.ID, "cntphmaster_btnSave")
                sc_submit_button.click()

                time.sleep(3)

                sc_next_button = driver.find_element(By.ID, "cntphmaster_BtnNext")
                sc_next_button.click()

                time.sleep(3)



            def thr_page():
                print(obj["thr_name"])

                dropdown_degselectone_input = Select(driver.find_element(By.ID, "cntphmaster_drpRefEduLevelId"))
                dropdown_degselectone_input.select_by_value("5")
                
                time.sleep(1)

                dropdown_degselecttow_input = Select(driver.find_element(By.ID, "cntphmaster_drpRefQualId"))
                dropdown_degselecttow_input.select_by_value("360")
                
                time.sleep(1)

                dropdown_degselectthree_input = Select(driver.find_element(By.ID, "cntphmaster_drpRefSpecificationId"))
                dropdown_degselectthree_input.select_by_value("1894")
                
                time.sleep(1)

                fn_input = driver.find_element(By.ID, "cntphmaster_txtQualYear")
                fn_input.send_keys(obj["grad_year"])

                #cntphmaster_txtQualYear

                thr_submit_button = driver.find_element(By.ID, "cntphmaster_btnSave")
                thr_submit_button.click()

                time.sleep(3)

                thr_next_button = driver.find_element(By.ID, "cntphmaster_BtnNext")
                thr_next_button.click()

                time.sleep(3)





            def las_page():
                print(obj["ls_name"])

                dropdown_degselectempone_input = Select(driver.find_element(By.ID, "cntphmaster_drpRefEmploymentTypeId"))
                dropdown_degselectempone_input.select_by_value("1")
                
                time.sleep(3)

                dropdown_degselectemptow_input = Select(driver.find_element(By.ID, "cntphmaster_drpEmployeeType"))
                dropdown_degselectemptow_input.select_by_value("18")
                
                time.sleep(1)

                def reverse_date(date_str):
                    # Split the date string into components
                    components = date_str.split("-")
                    # Reverse the components
                    reversed_components = components[::-1]
                    # Join the reversed components back into a string with dashes
                    reversed_date_str = "-".join(reversed_components)
                    return reversed_date_str

                # Example usage
                date = obj["st_date"].strip()
                reversed_date = reverse_date(date)
                print(reversed_date)
                time.sleep(1)

                fng_input = driver.find_element(By.ID, "cntphmaster_txtDateFrom")
                fng_input.send_keys(reversed_date)

                #cntphmaster_txtDateFrom

                dropdown_degselectempgtow_input = Select(driver.find_element(By.ID, "cntphmaster_drpCaoaJobcategoryId"))
                dropdown_degselectempgtow_input.select_by_value("4")
                
                time.sleep(1.5)

                dropdown_dgegselectemptow_input = Select(driver.find_element(By.ID, "cntphmaster_drpCaoaJobtypeId"))
                dropdown_dgegselectemptow_input.select_by_value("45")
                
                time.sleep(1.5)

                dropdown_dgegseletemptow_input = Select(driver.find_element(By.ID, "cntphmaster_drpCaoaJobgradeId"))
                dropdown_dgegseletemptow_input.select_by_value("8")
                
                time.sleep(1)

                fngoyt_input = driver.find_element(By.ID, "cntphmaster_txtFinancialDegreeDate")
                fngoyt_input.send_keys(reversed_date)

                drdown_dgseletptow_input = Select(driver.find_element(By.ID, "cntphmaster_drpCaoaJobtitleId"))
                drdown_dgseletptow_input.select_by_value("781403")
                
                time.sleep(1)

                ls_submit_button = driver.find_element(By.ID, "cntphmaster_btnSave")
                ls_submit_button.click()

                time.sleep(3)

                ls_next_button = driver.find_element(By.ID, "imgData_Emp_Vision")
                ls_next_button.click()

                time.sleep(3)

                #id="cntphmaster_Check_Revision" type="checkbox"

                # Locate the checkbox by its ID
                checkbox = driver.find_element(By.ID, "cntphmaster_Check_Revision")

                # Check if the checkbox is not already selected, then click to select it
                if not checkbox.is_selected():
                    checkbox.click()

                # Optionally, wait to observe the change (for demonstration purposes)
                time.sleep(2)

                # Switch to the alert
                alert = Alert(driver)

                # Accept the alert
                alert.accept()
                start_new_button = driver.find_element(By.ID, "cntphmaster_BtnNew")
                start_new_button.click()

                time.sleep(2)






                





            fr_page()
            sc_page()
            thr_page()
            las_page()
            print(obj)

            data_ork(operator)

        # Run the data_ork function to see the output
        data_ork()





        

        # Wait indefinitely to keep the browser open
        input("Press Enter to close the browser...")

    finally:
        # Close the browser
        driver.quit()

# Example usage:
url = "https://registration.caoa.gov.eg/UI/Guest/Login.aspx"
username = "gizhealth27"
password = "hero846"

perform_registration(url, username, password)
