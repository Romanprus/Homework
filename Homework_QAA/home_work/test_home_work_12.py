"""
Site = "https://www.demoblaze.com"

XPATH:
1. header_bar = //div[@id='navbarExample']
2. header_bar_home = "//li[@class='nav-item active']"
3. header_bar_contact = "//a[@data-target='#exampleModal']"
4. header_bar_about = "//a[@data-target='#videoModal']"
5. header_bar_cart = "//a[@id='cartur']"
6. header_bar_login = "//a[@data-target='#logInModal']"
7. header_sign_in ="//a[@id='signin2']"
8. footer_info = "//p[@class='m-0 text-center text-white']/parent:: footer"
9.main_menu_item_nokia = "//div[@id='tbodyid']/div[2]" # знаю що по ІД не шукаємо просто спробував щоб глянути я працює
10. main_menu_item_nexus = "//p[@id='article']//..//a[@href='prod.html?idp_=3']"
11. main_menu_button_next = "//button[@id='next2']"
12. main_menu_button_previous = "//button[@id='prev2']"
13. item_screen_add_button = "//a[@class='btn btn-success btn-lg']" # screen after clicking on any item/product screen
14. item_screen_image = "//div[@class='item active']"  # screen after clicking on any item/product screen
15. item_screen_description ="//div[@class='description description-tabs']" # screen after clicking on any item/product screen
16. card_screen_button= "//button[@class='btn btn-success']" #click on Cart in header that Xpath appear
17. //button[@onclick="logIn()"] # appear after clicking on login
18. //button[@onclick="send()"] # appear after clicking on Contact
19.//textarea # appear after clicking on Contact
20. //a[@onclick="deleteItem('7fce5537-b52b-42c3-ff1b-51ed77a2c2c5')"] # # after click on Card and some items in card
21//div[@class='item active']/ancestor:: div[@id="myCarousel-2"] #after click on any product
22//*[contains(text(), 'Samsung')] #https://www.demoblaze.com/cart.html and samsung is added to the cart
23 //button[text()='Sign up'] # after click on Sign up button
24//div[@id='signInModal']//span/parent::button[@aria-label='Close'] #after click on Sign up button
25 //div/descendant:: div[@class="vjs-poster"] # after click on About US
26//button[@title="Play Video"] # after click on About US
27//a[@data-slide="prev"]
28 //div[@id='carouselExampleIndicators']//span[text()='Next']
29//a[@id='nava']
30 //div[@class="col-lg-3"]/div/a[@class="list-group-item" and @onclick="byCat('monitor')" ]

 CSS:
 1. a#cat
2. [title='Play Video'] # after click on About US
3. 'div input#recipient-email' # after click on Sign up button
4. button[data-target="#orderModal"] # after click on Card
5. div a.navbar-brand[href="index.html"]
6. a[href="prod.html?idp_=1"]+div # main screen
7.li~li.page-item
8"div>input#recipient-name" #after click on Contact
9 button~button[onclick="send()"]  #after click on Contact
10 h4 [src="bm.png"]
11 div:last-child a[onclick="byCat('monitor')"]
12 div:first-child ol.carousel-indicators li[data-slide-to="1"]
13div#navbarExample li a#cartur
14#login2
15 #tbodyid div>a[href='prod.html?idp_=9']

"""

import time
from selenium.webdriver.common.by import By


def test_login(open_login_window):
    """" function for auto login on Chrome browse"""
    login_window = open_login_window
    all_courses = login_window.login("test_auto50@gmail.com", 'number2000')
    assert all_courses.user_avatar_is_visible() is True, 'User not login'


def test_search(open_login_window, search):
    login_window = open_login_window
    all_courses = login_window.login("test_auto50@gmail.com", 'number2000')
    main_screen = search.enter_something_in_search('Course')
    loop = main_screen
    assert loop == search.enter_something_in_search('Course')


def test_select_course(main_screen, play_video):
    all_courses = main_screen
    course = main_screen.choose_course()
    play = play_video.play_video()
    assert play.is_video_start() is True, "Click play button"

def test_register_user(open_register_window):
    register = open_register_window
    assert register.is_title_visible() is True, "Open Login window to procide registration"