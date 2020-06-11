*** Settings ***
Variables    Variables/cms.py
Resource     Cases/cms.robot
Test Template    getCategoryList_case


*** Test Cases ***

Invalid                  ${Invalid_Category_json}              ${domain_test}      200
Invalid filmId           ${Invalid_Category_filmId}            ${domain_test}      400
Invalid emptyfilmId      ${Invalid_Category_emptyfilmId}       ${domain_test}      500

