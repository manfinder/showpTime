from bs4 import BeautifulSoup

import os
import urllib.request,urllib.error,urllib.parse

url="https://www.time.ir/"
response=urllib.request.urlopen(url)
webContent=response.read().decode('UTF-8')



soup = BeautifulSoup(webContent, 'html.parser')
soup.prettify()
farsinumeral=soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate11cphTop_3917_lblShamsiNumeral").string
farsiDate=soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate11cphTop_3917_lblShamsi").string
sunset=soup.find(id="ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset").string
sunrise=soup.find(id="ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise").string
englishTime=soup.find(id="ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate11cphTop_3917_lblGregorian").string



print(farsinumeral)
print("Day : "+farsiDate)
print("Sunset time : "+sunset)
print("sunrise : "+sunrise)
print(englishTime)




