*** Settings ***
Library      RequestsLibrary
Library      Collections
Variables    Variables/cms.py
Resource     Cases/cms.robot
#Suite Setup
#Test Template    getCategoryList_case


*** Test Cases ***
getCategoryList_case
    [Documentation]   获取栏目列表
#    [Arguments]       ${json}         ${domain_test}      ${assert}
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${getCategoryList}[path]     headers=${getCategoryList}[header]    json=${Invalid_Category_json}
    ${respjson}    to json     ${resp.content}
    ${columnid}      Get From Dictionary    ${respjson}[data][0]     columnId
    Set Suite Variable	 &{Suite}     columnId=${columnid}
    log to console     ${Suite}
    Should Be Equal As Strings    ${resp.status_code}    200

getContentList_case
    [Documentation]   获取栏目列表
#    [Arguments]       ${json}         ${domain_test}      ${assert}
    create session    api       ${domain_test}
#    log to console    ${Global}[columnId]
    ${columnId}=	  Get From Dictionary		${Suite}    columnId
    Set To Dictionary      ${Invalid_Content_json}   columnId=${Suite}[columnId]
    ${resp}=          post request     api         ${getContentList}[path]     headers=${getCategoryList}[header]    json=${Invalid_Content_json}
    ${respjson}    to json     ${resp.content}
    Should Be Equal As Strings    ${resp.status_code}    200
