# Execute test cases & generate report files (JSON)
# Command::
            behave -f allure_behave.formatter:AllureFormatter -o reports/ features
            [behave -f allure_behave.formatter:AllureFormatter -o report_folder_name features_location]
# To Generate Allure Report:
            allure serve reports/ [allure serve report_folder]