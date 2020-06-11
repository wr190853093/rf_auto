*** Settings ***
Variables    Variables/cms.py
Resource     Cases/cms.robot
Test Template    getContentList_case

*** Test Cases ***

Invalid                  ${Invalid_json}                ${domain_test}      200
Invalid filmId           ${Invalid_Content_columnId}    ${domain_test}      400
