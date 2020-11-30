

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains


def load_cookie(driver, path):
	with open(path, 'rb') as cookiesfile:
		cookies = pickle.load(cookiesfile)
		for cookie in cookies:
			driver.add_cookie(cookie)


import platform
import os
import pickle
import time

def control_key():
	is_osx = platform.system().startswith('Darwin')
	return Keys.COMMAND if is_osx else Keys.CONTROL 


path_chromedriver = './chromedriver'
if os.path.exists(path_chromedriver):
	driver = webdriver.Chrome(executable_path = path_chromedriver)
else:
	driver = webdriver.Chrome(ChromeDriverManager().install()) 


##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################

'''
CHANGE PARAMETERS HERE 
'''

youtube_url = "http://www.youtube.com"
search_text = "baby delivery birth"
AN_comment_text_filename = "youtube_invite_welcome.txt"


''' 
THESE NEED TO BE CONSTANTLY UPDATED 
ACCORDING TO THE YOUTUBE VERSION UPGRADES
'''

youtube_search_xpath = "//div[@id='search-input']/input[@id='search']"
video_title_xpath = "//a[@id='video-title']"
new_comment_box = "//*[@id='simplebox-placeholder']"
new_comment_placeholder_anchor = "//*[@id='contenteditable-root'][@aria-label='Add a public comment...']"
comment_button = '//*/paper-button[@id="button"][@aria-label="Comment"]'


##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################



driver.get(youtube_url)
load_cookie(driver, './login_cookie')
search_box = driver.find_element_by_xpath(youtube_search_xpath)


search_box.clear()
search_box.send_keys(search_text)
search_box.send_keys(Keys.RETURN)

AN_comment_text = None

with open(AN_comment_text_filename, "r") as AN_comment_text_file:
	AN_comment_text = AN_comment_text_file.read()

done_URLs_map = {}
done_map_filename = "done_URLs_map"

if os.path.exists(done_map_filename):
	with open(done_map_filename, 'rb') as donemap_file:
		done_URLs_map = pickle.load(donemap_file)



# google_sign_in = "https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A17161db8298ee2f5%2C10%3A1606710313%2C16%3Af7160e3b648ac360%2Cbf04a3314e10c9058fbdbf6357387626395a3c7296c3b341691cdb1f3af97941%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22f39e8ec6c8974158ab2b5cf9f4b959e6%22%7D&response_type=code&flowName=GeneralOAuthFlow"


# driver.get(google_sign_in)

# print("Please login on browser and press any key to proceed !")
# proceed = input()


def fetch_video_urls():

	videos = []

	while True:

		driver.implicitly_wait(2) # seconds

		videos = driver.find_elements_by_xpath(video_title_xpath)

		videos = list(filter(lambda v : v.get_attribute('href') not in done_URLs_map.keys(), videos))

		for v in videos:

			if v.get_attribute('href') not in done_URLs_map:
				done_URLs_map[v.get_attribute('href')] = v
				yield v.get_attribute('href')


def open_and_comment_in_new_tab(video_url):
	# actions = ActionChains(driver)      
	# actions.key_down(control_key()).key_down('w').key_up('w').key_up(control_key()).perform()

	current_video_elem = done_URLs_map[video_url]

	current_video_elem.send_keys(control_key() + Keys.RETURN)

	#switch tab
	driver.switch_to.window(driver.window_handles[-1])

	print("opened new video in new tab !")

	print("switched to the newtab ! ready to comment ")

	delay = 3 # seconds
	browser = driver
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'info')))
		print("Page is ready!")
	except TimeoutException:
		print("Loading took too much time!")

	driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")

	driver.implicitly_wait(5) # seconds
	commentBox = driver.find_element_by_xpath(new_comment_box)
	commentBox.click()


	driver.implicitly_wait(2) # seconds
	new_comment_placeholder = driver.find_element_by_xpath(new_comment_placeholder_anchor)
	driver.execute_script("arguments[0].scrollIntoView();", new_comment_placeholder)
	new_comment_placeholder.send_keys(AN_comment_text)
	
	driver.find_element_by_xpath(comment_button).click()

	print("Inserted comment !")

	# close the tab
	driver.close()

	# OR :
	driver.switch_to.window(driver.window_handles[0])
	print("switched back to the main tab with search results ! ")
	driver.execute_script("arguments[0].scrollIntoView();", current_video_elem)

	# replace the web-element value by boolean to make it picklable
	done_URLs_map[video_url] = True

	with open(done_map_filename, 'wb') as donemap_file:
		pickle.dump(done_URLs_map, donemap_file)


for url in fetch_video_urls():

	open_and_comment_in_new_tab(url)


driver.close()

