from pkgutil import iter_modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

# IMPORT DATA
filepath = input('Enter filepath:')
data = pd.read_csv(f'{filepath}').replace(np.nan, '', regex=True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://web.budgetbakers.com/dashboard")
driver.maximize_window()
time.sleep(5)

# HTML ELEMENTS
fieldsExpense = {
    "account": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div.text", # added "> div.text" to selector
    "amount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(2) > div > div.ten.wide.field.field-amount.expense > div > input[type=text]",
    "currency": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(2) > div > div.six.wide.field.field-currency.small-select > div > div.text",
    "category": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div.field.select-category > div > div.text", # added "> div.text" to selector
    "labels": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div.text", # added "> d.v.text" to selector
    "date": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker-wrapper > div > input[type=text]",
    "time": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div.react-datepicker-wrapper > div > input[type=text]",
    "payee": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(1) > div > input[type=text]",
    "note": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div.field.field-note > textarea",
    "payType": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(3) > div > div > div.text", # added "> div.text" to selector
    "payStatus": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(4) > div > div > div.text" # added "> div.text" to selector
}

fieldsIncome = {
    "account": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div.text",
    "amount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(2) > div > div.ten.wide.field.field-amount.income > div > input[type=text]",
    "currency": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div > div:nth-child(2) > div > div.six.wide.field.field-currency.small-select > div > div.text",
    "category": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div.field.select-category > div > div.text", # added "> div.text" to selector
    "labels": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div.text", # added "> d.v.text" to selector
    "date": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker-wrapper > div > input[type=text]",
    "time": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div.react-datepicker-wrapper > div > input[type=text]",
    "payee": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(1) > div > input[type=text]",
    "note": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div.field.field-note > textarea",
    "payType": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(3) > div > div > div.text", # added "> div.text" to selector
    "payStatus": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(4) > div > div > div.text" # added "> div.text" to selector
}

fieldsTransfer = {
    "fromAccount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > div > div.text",
    "fromAmount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div.ten.wide.field.field-amount.transfer > div > input[type=text]",
    "fromCurrency": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div.six.wide.field.field-currency.small-select > div > div.text",
    "toAccount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div > div > div.text",
    "toAmount": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div.ten.wide.field.field-amount.transfer > div > input[type=text]",
    "toCurrency": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-color-panel > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > div.six.wide.field.field-currency.small-select > div > div.text",
    "labels": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div.text",
    "date": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.react-datepicker-wrapper > div > input[type=text]",
    "time": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div.react-datepicker-wrapper > div > input[type=text]",
    "payee": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(1) > div > input[type=text]",
    "note": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div.field.field-note > textarea",
    "payType": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(3) > div > div > div.text", # added "> div.text" to selector
    "payStatus": "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.six.wide.computer.sixteen.wide.mobile.six.wide.tablet.column.form-detail > form > div:nth-child(4) > div > div > div.text" # added "> div.text" to selector
}

# CLICK SEQUENCE
def clickSequence(field, value):
    actions = ActionChains(driver)
    actions.click(field)		
    actions.move_to_element(value)
    actions.click()
    actions.perform()

def changeType(typeId):
    # OPEN RECORDS
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/div/button").click()
    
    # CHANGE TYPE
    type = driver.find_element(by=By.XPATH,value=f"//div[@class='ui compact fluid inverted three item record-form-menu menu']/a[contains(text(),'{typeId}')]")
    type.click()

def updateValues(type, row, fields):
    # type
    if type == "transfer":
        accounts = ["toAccount", "fromAccount"]
        currencies = ["toCurrency", "fromCurrency"]
        textfields = ["toAmount", "fromAmount", "payee", "note"]
    else:
        accounts = ["account"]
        currencies = ["currency"]
        textfields = ["amount", "payee", "note"]

    # account       
    for item in accounts:
        account = driver.find_element(by=By.CSS_SELECTOR, value=fields[item])
        account_value = driver.find_element(by=By.XPATH, value=f"//div[@name='{item}Id']/div[2]/div[./div/div[position()=2 and contains(text(),'{row[item]}')]]")
        clickSequence(account, account_value)

    # currency
    for item in currencies:
        currency = driver.find_element(by=By.CSS_SELECTOR, value=fields[item])
        currency_value = driver.find_element(by=By.XPATH, value=f"//div[@name='{item}Id']/div[2]/div[./span[contains(text(),'{row[item]}')]]")
        clickSequence(currency, currency_value)

    # amount, payee, note
    for item in textfields:
        textfield = driver.find_element(by=By.CSS_SELECTOR, value=fields[item])
        textfield.clear()
        textfield.send_keys(row[item])
    
    # category
    if type != "transfer":
        driver.find_element(by=By.CSS_SELECTOR, value=fields["category"]).click()
        searchbar = "body > div.ui.page.modals.dimmer.transition.visible.active > div > div.add-record-content.content > div > div.ten.wide.computer.sixteen.wide.mobile.ten.wide.tablet.column.form-main > form > div.main-white-panel > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div.field.select-category > div > div.default.text > div > div > input[type=text]"
        category_search = driver.find_element(by=By.CSS_SELECTOR, value=searchbar)
        category_search.click()
        category_search.send_keys(row["category"].split(' ')[0])
        driver.find_element(by=By.XPATH, value="//div[@class='field select-category ']/div/div[2]/div/ul/li[1]/div").click()

    # labels
    labels = row["labels"]
    if labels:
        items = labels.strip().replace(', ',',').replace(' ,',',').split(',')
        label = driver.find_element(by=By.CSS_SELECTOR, value=fields["labels"])
        actions = ActionChains(driver)
        actions.click(label)		
        for item in items:
            label_value = driver.find_element(by=By.XPATH, value=f"//div[@name='labels']/div[2]/div[./span[contains(text(),'{item}')]]")
            actions.move_to_element(label_value)
            actions.click()
            actions.perform()

    # Payment Type
    payType = driver.find_element(by=By.CSS_SELECTOR, value=fields["payType"])
    payType_value = driver.find_element(by=By.XPATH, value=f"//div[@name='paymentType']/div[2]/div[contains(text(),'{row['payType']}')]")
    clickSequence(payType, payType_value)

    # Payment Status
    payStatus = driver.find_element(by=By.CSS_SELECTOR, value=fields["payStatus"])
    payStatus_value = driver.find_element(by=By.XPATH, value=f"//div[@name='recordState']/div[2]/div[contains(text(),'{row['payStatus']}')]")
    clickSequence(payStatus, payStatus_value)

    '''
    For fields not directly using <input> fields, execute_script() method was used to assign value,
    bypassing the need to select from the date and time selector
    UPDATE:
    values are being overridden when using execute_script()
    method is reverted back to send_keys(), with a click() prior to the method
    '''
    # date
    entryDate = driver.find_element(by=By.CSS_SELECTOR, value=fields["date"])
    entryDate.click()
    driver.execute_script("arguments[0].value=arguments[1]", entryDate, "")
    entryDate.clear()
    entryDate.send_keys(row["date"])
    entryDate.send_keys(Keys.ENTER)
        
    # time
    entryTime = driver.find_element(by=By.CSS_SELECTOR, value=fields["time"])
    entryTime.click()
    entryTime_value = driver.find_element(by=By.XPATH, value=f"//ul[@class='react-datepicker__time-list']/li[contains(text(),'{row['time']}')]")
    clickSequence(entryTime, entryTime_value)

    # ADD RECORD
    #time.sleep(3)
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/button").click()


# == SELENIUM SEQUENCE ==
# LOGIN
load_dotenv(dotenv_path="../.env")
name = os.getenv("APP_USERNAME")
pw = os.getenv("APP_PASSWORD")
main = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.NAME, "email"))
)
driver.find_element(by=By.NAME, value="email").send_keys(name)
driver.find_element(by=By.NAME, value="password").send_keys(pw)
#driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div[3]/div/div/form/button").click()
driver.find_element(by=By.XPATH, value="/html/body/div/div/div/section/div/form/button").click()


main = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/button"))
)

for index_base, row in data.iterrows():
    index = index_base + 2
    # SELECT TYPE
    try:
        if row["type"] == "Expense":
            changeType("Expense")
            updateValues("expense", row, fieldsExpense)
            print(f"Row {index} -- OK")
            data.loc[index-2, 'type'] = 'Expense -- OK'

        elif row["type"] == "Income":
            changeType("Income")
            updateValues("income", row, fieldsIncome)
            print(f"Row {index} -- OK")
            data.loc[index-2, 'type'] = 'Income -- OK'

        elif row["type"] == "Transfer":
            changeType("Transfer")
            updateValues("transfer", row, fieldsTransfer)
            print(f"Row {index} -- OK")
            data.loc[index-2, 'type'] = 'Transfer -- OK'

        else:
            # SKIP
            print(f"Row {index} is skipped.")

    except:
        driver.find_element(by=By.CSS_SELECTOR, value="body > div.ui.page.modals.dimmer.transition.visible.active > div > div.header > span").click()
        print(f"Row {index} -- ERROR!!")

driver.close()

data.to_csv(f'{filepath}_out', index=False)

'''
NOTES:
- execute_script() for non-input tags
- remember to click the field before using send_keys()
- types of xpath search
account_value = driver.find_element(by=By.XPATH, value=f"//div[@name='accountId']/div[2]/div[./div/div[position()=2 and contains(text(),'{row['account']}')]]") ## NESTED
account_value = driver.find_element(by=By.XPATH, value="//div[@name='accountId']/div[2]/div[.//div[contains(text(),'Tonik')]]")        ## FIND DESCENDANT
'''
