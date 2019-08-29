from selenium import webdriver

url = input('Input ASKERS URL : ')
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

driver.get('url')

ans_css = 'body > app-root > div > div.main-container > app-post-list > div.container > div > div > div.card-list.mt-2 > div > div:nth-child(NUM) > app-post-detail > div.card-body > div.card-title > p > p'
comment_css = 'body > app-root > div > div.main-container > app-post-list > div.container > div > div > div.card-list.mt-2 > div > div:nth-child(POST_NUM) > app-post-detail > div.card-body > app-reply-list > app-reply-detail:nth-child(COMMENT_NUM) > div > div.card-title > p > p'

num = 1

file_num = 1

while(1):
    try:
        comment_num = 1
        ans_id = ans_css.replace('NUM', str(num))
        ans = driver.find_element_by_css_selector(ans_id).text
        comment = []
        while(1):
            try:
                comment_id = comment_css.replace('POST_NUM',str(num)).replace('COMMENT_NUM', str(comment_num))
                #print(comment_id)
                comment.append(driver.find_element_by_css_selector(comment_id).text)
                comment_num += 1
            
            except:
                break
                
        if len(comment) != 0:
            file_name = '질문 ' + str(file_num) + '.txt'
            f = open(file_name, 'w')
            f.write('<질문>\n')
            f.write(ans + '\n\n')

            f.write('<답변>\n')
            for i in comment:
                f.write(i+'\n\n')
            f.close()
            file_num += 1
 
        num += 1
    except:
        break

