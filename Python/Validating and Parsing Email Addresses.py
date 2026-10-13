from email.utils import parseaddr, formataddr
import re
def main():
    n = int(input())

    for i in range(0,n):
        st = input()
        #name, email = st.split('<')
        #print(name, email)
        name, email = parseaddr(st)
        namematched = re.search(r'[a-zA-z]+[a-zA-z0-9-_]+', name)
        domainandextensionmatched = re.search(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email) 
        if namematched != None and domainandextensionmatched != None:
            print(formataddr((namematched.group(), domainandextensionmatched.group())))

if __name__ == '__main__':
    main()
