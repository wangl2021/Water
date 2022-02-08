# -*- coding: utf8 -*-
import time
import xlrd
from selenium import webdriver
import time
def read_excel():
    # data = xlrd.open_workbook(filename)  # 打开xls文件
    # sheet = data.sheets()[0]  # 打开第一张表
    # rows = sheet.nrows  # 获取表的行数
    # cols = sheet.ncols  # 获取表的列数
    # nrows = bytes(rows)
    # ncols = bytes(cols)
    # print("共:"+nrows+"行,  "+ncols+"列")
    #for i in range(rows):
    # for i in range(3):
    #     if i == 0:
    #         continue
    #     for j in range(cols - 1):
    #         ctype = sheet.cell(i, j).ctype  # 表格的数据类型
    #         cell = sheet.cell_value(i, j)
    #         if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
    #             cell = int(cell)  # 浮点转成整型
    #         cell = bytes(cell)
    url="http://news.baidu.com/"
    print(url)
    browser = webdriver.Firefox()
    # browser = webdriver.PhantomJS(executable_path=r'D:\data\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    time.sleep(5)
    browser.set_window_size(1200, 714)
    browser.get(url)  # Load page
    time.sleep(2)


    # time.sleep(5)

    # browser.execute_script("""
    #         (function () {
    #             var y = 0;
    #             var step = 100;
    #             window.scroll(0, 0);
    #
    #             function f() {
    #                 if (y < document.body.scrollHeight) {
    #                     y += step;
    #                     window.scroll(0, y);
    #                     setTimeout(f, 100);
    #                 } else {
    #                     window.scroll(0, 0);
    #                     document.title += "scroll-done";
    #                 }
    #             }
    #
    #             setTimeout(f, 1000);
    #         })();
    #     """)

    for i in range(1, 30):
        if "scroll-done" in browser.title:
            browser.close()
            break
        else:
            time.sleep(2)
            client_height = browser.execute_script("return $(document).scrollTop();")
            client_height1 = browser.execute_script("return  $(window).height();")

            print(client_height,client_height1)
            js = "var q=document.documentElement.scrollTop=%s" % (client_height+client_height1)
            name = time_info()
            dir_url = "D:\\code\\%s.png" % name
            browser.execute_script(js)
            browser.save_screenshot(dir_url)

        time.sleep(10)


    # browser.execute_script("""
    #         $('#main').siblings().remove();
    #         $('#aside__wrapper').siblings().remove();
    #         $('.ui.sticky').siblings().remove();
    #         $('.follow-me').siblings().remove();
    #         $('img.ui.image').siblings().remove();
    #         """)

    # print(dir_url)
    browser.close()


def time_info():
    ti = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(ti)
    return str(ti)
if __name__ == "__main__":

    read_excel()