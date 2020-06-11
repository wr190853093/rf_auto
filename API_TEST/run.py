import os
import sys
import pathlib
import json
import arrow


# class ITest(unittest.TestCase):
#     try:
#         proj_name = sys.argv[1]
#         try:
#             if len(sys.argv) > 2:
#                 if sys.argv[2] == 'smoke':
#                     # BuildSmoke().getCaseJson(proj_name)
#                     f = open(f'./cases/{proj_name}/cases-smoke.json', 'r', encoding='UTF-8')
#             else:
#                 f = open(f'./cases/{proj_name}/cases.json', 'r', encoding='UTF-8')
#
#             s = json.load(f)
#             cases = s['Cases']
#             if cases:
#                 for case in cases:
#                     test_id = case.get('TestId', None)
#                     desc = case.get('Desc', None)
#                     state = case.get('State', 1)
#                     if test_id:
#
#                         exec(f'''@unittest.skipUnless({state},'state值为0,跳过测试')\ndef test_{test_id}(self):
#                                 '{desc}'
#                                 BuildCase().execute_case({case},'{proj_name}')
#                                 ''')
#                     else:
#                         print('测试用例缺少id')
#             else:
#                 print('无可执行的测试用例')
#         except Exception as e:
#             print('读取用例数据失败:', e)
#
#     except Exception:
#         print("请输入要执行的项目名,格式 run.py project")


if __name__ == '__main__':

    try:
        task = sys.argv[1]
        s = pathlib.Path(".")/'robot'
        # os.system(f"{s} --outputdir ./Reports/{task}/{arrow.now().format('YYYYMMDD_HHmmss')} --pythonpath . ./Tasks/{task}.robot")
        os.system(
            f"{s} --outputdir ./Reports/{task} --pythonpath . ./Tasks/{task}.robot")

    except BaseException:
        #raise Exception("请输入要执行的项目名,格式 run.py project")
        print("请输入要执行的任务名,格式 run.py task_name")
