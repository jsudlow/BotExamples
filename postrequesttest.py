import requests,time

from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url = "https://www.supremenewyork.com/shop/jackets/o459bkd8n/p5eiyuxlj"
post_url = "https://www.supremenewyork.com/shop/173165/add"

# construct the POST request
form_data = {
    'utf8' : '%E2%9C%93',
    'authenticity_token': 0,
    'h' : 1,
    'st' : 27062,
    's' : 77982
} 



with requests.session() as s:
    
    #r = s.get(url)
    #print r.text.encode('ascii','ignore')
    #soup = BeautifulSoup(r.text,'html.parser')    
    #form = soup.find('form')
    #auth_token = form.find('input', {'name' : 'authenticity_token'}).get('value').encode('ascii','ignore')
    #action=  form.get('action')
    #apost_url = "https://www.supremenewyork.com" + action
    #print apost_url
    #rint 'sleeping 2 seconds'
    #time.sleep(2)
    #print 'sleeping for 2 seconds \n'
    #form_data['authenticity_token'] = 0
    
    print 'this is the form we are about to send'
    print form_data
    print 'about to start the clock'
    start =  time.clock()
    post = s.post(post_url,data=form_data)
    response_time = time.clock() - start
    print 'The response time for the post was: ',response_time,'\n'
    print post
    print post.text
    time.sleep(2)
    cart_page = s.get('https://www.supremenewyork.com/shop/cart')
    print cart_page.text