# Phonebook.cz Scraper
<b>phonebook.py</b> is a  <a href="https://phonebook.cz">phonebook.cz</a> scraper tool which queries the phonebook.cz search engine and scrapes all items from page.

## Update 4/27/23
When you visit the site now you will see this note:

![image](https://user-images.githubusercontent.com/34954477/235016173-6fcfb85d-f7d6-490e-a763-9e843ad0b589.png)

You now need to auth to intelx.io then grab the auto token from the http response. Insert that into this tool and you will be able to scrape again!

## phonebook.py usage:
```
usage: phonebook.py [-h] [-e EMAIL] [-d DOMAIN] [-l LINKS] [-o [PHONEBOOK_CZ]]

Phonebook.cz scraper

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Search all emails for this domain.
  -d DOMAIN, --domain DOMAIN
                        Search all subdomains for this domain.
  -l LINKS, --links LINKS
                        Search all links for this domain.
  -o [PHONEBOOK_CZ], --outfile [PHONEBOOK_CZ]
                        Stores all items in file *_cz.txt
```
   Scrape emails:
      
    $ python3 phonebook.py -e contoso.com
     [+] Running phonebook.cz scraper!
      
      someone@contoso.com
      shop@contoso.com
      edt@contoso.com
      mithbates@contoso.com
      hank.carbeck@contoso.com
      mario@contoso.com
      russell@contoso.com
      danielle.tiedt@contoso.com
      ronald@contoso.com
      scott.bishop@contoso.com
      
      [+] Done! Saved to to phonebook_cz.txt
      
   Scrape subdomains:
   
     $ python3 phonebook.py -d contoso.com -o 
      [+] Running phonebook.cz scraper!
      
      d2.contoso.com
      cont-ex01.corp.contoso.com
      dom1.contoso.com
      dom2.contoso.com
      site2-dc2.contoso.com
      site1-dc1.contoso.com
      delta.contoso.com
      clent1.contoso.com
      users1.contoso.com
      user1.contoso.com
      apollo.contoso.com
      publicdns.contoso.com
      
      [+] Done! Saved to to phonebook_cz.txt
      
  Scrape links from all logged domains:
  
     $ python3 phonebook.py -l contoso.com -o saveme
      [+] Running phonebook.cz scraper!
      
      https://exch01.contoso.com
      https://mail.contoso.com/ECP/
      http://media.marketing.contoso.com/file.wmv
      https://test-url.contoso.com
      https://login-east.contoso.com
      https://clm.contoso.com/CLM
      http://clm.contoso.com/CLM
      https://login-west.contoso.com
      https://login.contoso.com
      https://lh_pki1.contoso.com/certsrv
      https://extranet.contoso.com
      https://login.contoso.com/new

      [+] Done! Saved to to saveme_cz.txt
