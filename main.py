from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = email
        self.password = password
        self.browser.delete_all_cookies()


    def signIn(self):
        #Open the instagram login page
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        #sleep for 3 seconds to prevent issues with the server
        time.sleep(3)
        #Find username and password fields and set their input using our constants
        username = self.browser.find_element_by_name('username')
        username.send_keys(self.username)
        password = self.browser.find_element_by_name('password')
        password.send_keys(self.password)
        #Get the login button
        try:
            button_login = self.browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        except:
            button_login = self.browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')
        #sleep again
        time.sleep(2)
        #click login
        button_login.click()
        time.sleep(3)
        #In case you get a popup after logging in, press not now.
        #If not, then just return
        try:
            notnow = self.browser.find_element_by_css_selector(
                'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click()
        except:
            return


    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def unfollowWithUsername(self, username):
      self.browser.get(username)
      time.sleep(2)
      followButton = self.browser.find_element_by_css_selector('button')
      if (followButton.text == 'Following'):
          followButton.click()
          time.sleep(2)
          confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
          confirmButton.click()
          return 1
      else:
          print("You are not following this user")
          return 0

    def findFollowing(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers

    def unFollow(self, max, pause, grab):

        followed = 0

        while (followed < max):
                following = bot.findFollowing(self.username, grab)

                for x in range(0,len(following)):
                    target = following[x]
                    print(target)
                    time.sleep(pause)
                    result = bot.unfollowWithUsername(target)
                    if result == 1:
                        followed +=1

                time.sleep(pause*3)

bot = InstagramBot('demper.silencers', 'DEMPER2019SOCIAL')
bot.signIn()
#bot.followWithUsername('therock')
#bot.unfollowWithUsername('therock')
bot.unFollow(150,7,10)
