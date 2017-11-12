# coding:utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_block_adv
from runtime.fetcher import fetch
import datetime
import time


code = QA_fetch_stock_block_adv().code
x = fetch.QA_Tdx_Executor()

for i in range(100000):
    _time = datetime.datetime.now()
    #data = x.get_realtime(code)
    data = x.get_realtime_concurrent(code)
    # if data is not None:
    # print(len(data))
    # print(data[0])
    print('Time {}'.format((datetime.datetime.now() - _time).total_seconds()))
    time.sleep(1)
    print('Connection Pool NOW LEFT {} Available IP'.format(x._queue.qsize()))
    print('Program Last Time {}'.format(
        (datetime.datetime.now() - _time1).total_seconds()))
    # print(threading.enumerate())
#
