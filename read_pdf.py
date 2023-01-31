import PyPDF2 as pdf

def info(arch):
    '''
    arch=PDF file to be read \n\n
    return a dictionary with info= {page:content}
    '''
    content={}
    a=open(arch,'rb')
    b=pdf.PdfReader(a)
    print(len(b.pages))
    for c in range(len(b.pages)):
        print('page',c+1)
        content['page_'+str(c+1)]=b.pages[c].extract_text()
    
    return content


if __name__=='__main__':
    print('local')
    a=info(r'calendario_admin.pdf')
    print(type(a))
    print(a)