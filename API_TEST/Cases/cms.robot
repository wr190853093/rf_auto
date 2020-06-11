*** Settings ***
Library      RequestsLibrary
Library      Collections
Variables    Templates/ApiCms.py


*** Keywords ***

getCategoryList_case
    [Documentation]   获取栏目列表
    [Arguments]       ${json}         ${domain_test}      ${assert}
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${getCategoryList}[path]     header=${getCategoryList}[header]    json=${json}
    Should Be Equal As Strings    ${resp.status_code}    ${assert}

getContentList_case
    [Documentation]   获取内容列表
    [Arguments]       ${json}         ${domain_test}      ${assert}
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${getContentList}[path]     header=${getContentList}[header]    json=${json}
    Should Be Equal As Strings    ${resp.status_code}    ${assert}

getCategoryList_getContentList_case
    [Arguments]       ${json}         ${domain_test}      ${assert}
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${getCategoryList}[path]     header=${getCategoryList}[header]    json=${json}
    Should Be Equal As Strings    ${resp.status_code}    ${assert}
