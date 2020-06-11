*** Settings ***
Library      RequestsLibrary
Library      Collections
Variables    Templates/ApiBi.py


*** Keywords ***

biClientLoginoutReport_case
    [Documentation]   客户端启动退出
    [Arguments]      ${domain_test}   ${header}     ${json}
    create session    api       ${domain_test}
    ${resp}=          POST request     api         ${biClientLoginoutReport}[path]     headers=${header}    json=${json}
    ${respjson}    to json     ${resp.content}
    ${code}      Get From Dictionary    ${respjson}     code
    log Many    url=${resp.url}
    ...         body=${json}
    ...         respon=${respjson}
    Should Be Equal As Strings    ${code}    1000

biHeartclientUserHeart_case
    [Documentation]   客户端启动退出心跳
    [Arguments]      ${domain_test}   ${header}     ${json}    ${assert}    ${sleep}
    sleep    ${sleep}s
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${biHeartclientUserHeart}[path]     headers=${header}    json=${json}
    ${respjson}    to json     ${resp.content}
    ${code}      Get From Dictionary    ${respjson}     code
    log Many     url=${resp.url}
    ...          body=${json}
    ...         respon=${respjson}
    Should Be Equal As Strings    ${code}    ${assert}

biVideoOperationReport_case
    [Documentation]   播放视频信息上报
    [Arguments]      ${domain_test}   ${header}     ${json}    ${assert}
    create session    api       ${domain_test}
    ${resp}=          post request     api         ${biVideoOperationReport}[path]     headers=${header}    json=${json}
    ${respjson}    to json     ${resp.content}
    ${code}      Get From Dictionary    ${respjson}     code
    log Many     url=${resp.url}
    ...          body=${json}
    ...          respon=${respjson}
    Should Be Equal As Strings    ${code}    ${assert}


#getContentList_case
#    [Documentation]   获取内容列表
#    [Arguments]       ${json}         ${domain_test}      ${assert}
#    create session    api       ${domain_test}
#    ${resp}=          post request     api         ${getContentList}[path]     header=${getContentList}[header]    json=${json}
#    Should Be Equal As Strings    ${resp.status_code}    ${assert}
#
#getCategoryList_getContentList_case
#    [Arguments]       ${json}         ${domain_test}      ${assert}
#    create session    api       ${domain_test}
#    ${resp}=          post request     api         ${getCategoryList}[path]     header=${getCategoryList}[header]    json=${json}
#    Should Be Equal As Strings    ${resp.status_code}    ${assert}
