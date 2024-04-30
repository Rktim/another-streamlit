import streamlit as st

def morse_converter(txt):
    a={' ':'    ','a':'._','b':'_ ...','c':'_ . _ .','d':'_ ..','e':'.','f':'. _ .','g':'_ _ .','h':'....','i':'..','j':'_ . _ .','k':'_ . _','l':'. _ . .','m':'_ _','n':'_ .','o':'_ _ _','p':'. _ _ .','q':'_ _ . _','r':'. _ .','s':'...','t':'_','u':'.. _','v':'..._','w':'._ _','x':'_ .._','y':'_ . _ _','z':'_ _ ..','0':'_ _ _ _ _','1':'._ _ _ _','2':'.._ _ _','3':'..._ _','4':'...._','5':'.....','6':'_ ....','7':'_ _ ...','8':'_ _ _ ..','9':'_ _ _ _ .'}

    m_code=""
    for i in txt:
        m_code += a[i.lower()]

    return m_code

st.title("Convert your text to Morse-code.")

txt = st.text_input("Enter your text:")
morse_code = morse_converter(txt)

st.write("Your text  🙂‍↔️:", txt,height=50)
st.text_area("Morse code  🖱️:", morse_code,height=50)