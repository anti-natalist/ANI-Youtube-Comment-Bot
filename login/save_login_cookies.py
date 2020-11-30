from selenium import webdriver

import pickle

def save_cookie(driver, path):
	with open(path, 'wb') as filehandler:
		pickle.dump(driver.get_cookies(), filehandler)

#google_sign_in = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
#google_sign_in = "https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A17161db8298ee2f5%2C10%3A1606710313%2C16%3Af7160e3b648ac360%2Cbf04a3314e10c9058fbdbf6357387626395a3c7296c3b341691cdb1f3af97941%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22f39e8ec6c8974158ab2b5cf9f4b959e6%22%7D&response_type=code&flowName=GeneralOAuthFlow"

youtube_sign_in = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Faccount%26feature%3Dredirect_login&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

path_chromedriver = './chromedriver'
driver = webdriver.Chrome(executable_path = path_chromedriver)


oAuth_Login = "https://accounts.google.com/signin/v2/identifier?service=lbc&passive=1209600&continue=https%3A%2F%2Fbusiness.google.com%2F%3FskipPagesList%3D1%26gmbsrc%3Dbr-pt_BR-et-gs-z-gmb-l-z-h~my%257Credirect%257Cu%26skipLandingPage%3Dtrue%26hl%3Dpt-BR%26_ga%3D2.141175602.1643202833.1576602194-1983352456.1576602194&followup=https%3A%2F%2Fbusiness.google.com%2F%3FskipPagesList%3D1%26gmbsrc%3Dbr-pt_BR-et-gs-z-gmb-l-z-h~my%257Credirect%257Cu%26skipLandingPage%3Dtrue%26hl%3Dpt-BR%26_ga%3D2.141175602.1643202833.1576602194-1983352456.1576602194&hl=pt-BR&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

oAuth_google = "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
driver.get(oAuth_google)

foo = input()

google_home = "https://www.youtube.com/"
driver.get(google_home)

save_cookie(driver, './login_cookie')

driver.close()